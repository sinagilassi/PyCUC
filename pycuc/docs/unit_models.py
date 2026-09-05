"""Models used by the dimensional unit engine."""

from dataclasses import dataclass
from typing import TypeAlias

Dim: TypeAlias = tuple[int, int, int, int, int, int, int]

DIMENSIONLESS: Dim = (0, 0, 0, 0, 0, 0, 0)
MASS: Dim = (1, 0, 0, 0, 0, 0, 0)
LENGTH: Dim = (0, 1, 0, 0, 0, 0, 0)
TIME: Dim = (0, 0, 1, 0, 0, 0, 0)
CURRENT: Dim = (0, 0, 0, 1, 0, 0, 0)
TEMPERATURE: Dim = (0, 0, 0, 0, 1, 0, 0)
AMOUNT: Dim = (0, 0, 0, 0, 0, 1, 0)
LUMINOSITY: Dim = (0, 0, 0, 0, 0, 0, 1)


@dataclass(frozen=True, slots=True)
class UnitDefinition:
    symbol: str
    dimension: Dim | None = None
    definition: str | None = None
    scale: float = 1.0
    # Scale of a temperature interval to kelvin, when the unit is affine.
    interval_scale: float | None = None
    prefixable: bool = False
    aliases: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ResolvedUnit:
    dimension: Dim
    factor_to_si: float


def multiply(left: ResolvedUnit, right: ResolvedUnit) -> ResolvedUnit:
    a, b, c, d, e, f, g = left.dimension
    h, i, j, k, l, m, n = right.dimension
    dimension: Dim = (a + h, b + i, c + j, d + k, e + l, f + m, g + n)
    return ResolvedUnit(dimension, left.factor_to_si * right.factor_to_si)


def divide(left: ResolvedUnit, right: ResolvedUnit) -> ResolvedUnit:
    a, b, c, d, e, f, g = left.dimension
    h, i, j, k, l, m, n = right.dimension
    dimension: Dim = (a - h, b - i, c - j, d - k, e - l, f - m, g - n)
    return ResolvedUnit(dimension, left.factor_to_si / right.factor_to_si)


def power(unit: ResolvedUnit, exponent: int) -> ResolvedUnit:
    a, b, c, d, e, f, g = unit.dimension
    dimension: Dim = (
        a * exponent, b * exponent, c * exponent, d * exponent,
        e * exponent, f * exponent, g * exponent,
    )
    return ResolvedUnit(dimension, unit.factor_to_si ** exponent)
