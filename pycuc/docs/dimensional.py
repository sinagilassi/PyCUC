"""Recursive dimensional unit resolution and conversion."""

from functools import lru_cache
import math

from .refsx import RefsX
from .unit_errors import (AffineUnitError, CyclicUnitDefinitionError,
                          DimensionMismatchError, UnknownUnitError, UnitSyntaxError)
from .unit_models import (DIMENSIONLESS, ResolvedUnit, UnitDefinition, divide,
                          multiply, power)
from .unit_parser import Atom, Expression, Group, normalize_unit_expression, parse_unit_expression


def _registry() -> dict[str, UnitDefinition]:
    return {symbol: UnitDefinition(symbol=symbol, **details)
            for symbol, details in RefsX._unit_definitions_ref.items()}


def _apply_expression_aliases(expr: str) -> str:
    """Expand documented legacy spellings before strict syntax parsing."""
    exact = RefsX._expression_aliases_ref.get(expr)
    if exact is not None:
        return exact
    for alias, replacement in RefsX._expression_aliases_ref.items():
        expr = expr.replace(alias, replacement)
    return expr


def validate_unit_registry() -> None:
    registry = _registry()
    aliases: set[str] = set()
    for symbol, definition in registry.items():
        if not symbol or not math.isfinite(definition.scale) or definition.scale <= 0:
            raise ValueError(f"Invalid unit definition for {symbol!r}")
        if definition.interval_scale is not None and (
                not math.isfinite(definition.interval_scale) or definition.interval_scale <= 0):
            raise ValueError(f"Invalid interval scale for {symbol!r}")
        if definition.dimension is not None and (len(definition.dimension) != 7 or
                                                 not all(isinstance(x, int) for x in definition.dimension)):
            raise ValueError(f"Invalid dimension for {symbol!r}")
        if definition.dimension is not None and definition.definition is not None:
            raise ValueError(
                f"Unit {symbol!r} cannot have both dimension and definition")
        if definition.dimension is None and definition.definition is None:
            raise ValueError(f"Unit {symbol!r} has no dimensional definition")
        if not isinstance(definition.prefixable, bool):
            raise ValueError(f"Invalid prefixable value for {symbol!r}")
        for alias in definition.aliases:
            if not alias or alias in registry or alias in aliases:
                raise ValueError(f"Conflicting alias {alias!r}")
            aliases.add(alias)
    for definition in registry.values():
        if definition.definition:
            parse_unit_expression(definition.definition)
    for symbol in registry:
        _resolve_atom(symbol, False, ())


def _alias_map(registry: dict[str, UnitDefinition]) -> dict[str, str]:
    return {alias: definition.symbol for definition in registry.values() for alias in definition.aliases}


def _resolve_atom(symbol: str, compound_context: bool, stack: tuple[str, ...]) -> ResolvedUnit:
    if symbol == "1":
        return ResolvedUnit(DIMENSIONLESS, 1.0)
    registry = _registry()
    aliases = _alias_map(registry)
    canonical = aliases.get(symbol, symbol)
    prefix_scale = 1.0
    if canonical not in registry:
        for prefix, exponent in sorted(RefsX._prefixes_ref.items(), key=lambda item: len(item[0]), reverse=True):
            if canonical.startswith(prefix) and canonical[len(prefix):] in registry:
                candidate = registry[canonical[len(prefix):]]
                if candidate.prefixable:
                    prefix_scale = 10.0 ** exponent
                    canonical = candidate.symbol
                    break
        else:
            raise UnknownUnitError(f"Unknown unit {symbol!r}")
    if canonical in stack:
        raise CyclicUnitDefinitionError(
            "Cyclic unit definition detected: " + " -> ".join((*stack, canonical)))
    definition = registry[canonical]
    if canonical in {"C", "F", "R"} and compound_context:
        assert definition.dimension is not None and definition.interval_scale is not None
        return ResolvedUnit(definition.dimension, prefix_scale * definition.interval_scale)
    if definition.dimension is not None:
        return ResolvedUnit(definition.dimension, prefix_scale * definition.scale)
    assert definition.definition is not None
    resolved = _resolve_expression(parse_unit_expression(
        definition.definition), True, (*stack, canonical))
    return ResolvedUnit(resolved.dimension, prefix_scale * definition.scale * resolved.factor_to_si)


def _resolve_factor(factor: Atom | Group, compound_context: bool, stack: tuple[str, ...]) -> ResolvedUnit:
    if isinstance(factor, Atom):
        return power(_resolve_atom(factor.symbol, compound_context, stack), factor.exponent)
    return power(_resolve_expression(factor.expression, True, stack), factor.exponent)


def _resolve_expression(expression: Expression, compound_context: bool, stack: tuple[str, ...]) -> ResolvedUnit:
    result = ResolvedUnit(DIMENSIONLESS, 1.0)
    context = compound_context or len(
        expression.numerator) + len(expression.denominator) > 1 or bool(expression.denominator)
    for factor in expression.numerator:
        result = multiply(result, _resolve_factor(factor, context, stack))
    for factor in expression.denominator:
        result = divide(result, _resolve_factor(factor, True, stack))
    return result


@lru_cache(maxsize=2048)
def resolve_unit_expression(expr: str) -> ResolvedUnit:
    normalized = normalize_unit_expression(expr)
    normalized = _apply_expression_aliases(normalized)
    return _resolve_expression(parse_unit_expression(normalized), False, ())


def _is_standalone_affine(expr: str) -> bool:
    parsed = parse_unit_expression(expr)
    return (not parsed.denominator and len(parsed.numerator) == 1 and
            isinstance(parsed.numerator[0], Atom) and parsed.numerator[0].exponent == 1 and
            parsed.numerator[0].symbol in {"C", "F", "R"})


def convert_dimensional(value: float, from_unit: str, to_unit: str) -> float:
    normalized_from = normalize_unit_expression(from_unit)
    normalized_to = normalize_unit_expression(to_unit)
    normalized_from = _apply_expression_aliases(normalized_from)
    normalized_to = _apply_expression_aliases(normalized_to)
    if _is_standalone_affine(normalized_from) or _is_standalone_affine(normalized_to):
        raise AffineUnitError(
            "Standalone absolute temperature conversion is affine; use convert_from_to() or to()."
        )
    source = resolve_unit_expression(normalized_from)
    target = resolve_unit_expression(normalized_to)
    if source.dimension != target.dimension:
        raise DimensionMismatchError(
            f"Cannot convert {from_unit!r} to {to_unit!r}: dimensions are not compatible."
        )
    return float(value) * source.factor_to_si / target.factor_to_si
