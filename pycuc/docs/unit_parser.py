"""Strict tokenizer and parser for multiplicative unit expressions."""

from dataclasses import dataclass
import re

from .unit_errors import UnitSyntaxError

_SUPERSCRIPTS = set("\u00b9\u00b2\u00b3\u2070\u2071\u2074\u2075\u2076\u2077\u2078\u2079\u207b")
_ATOM = re.compile(r"[A-Za-z\u00b5\u03bc][A-Za-z0-9\u00b5\u03bc]*")


@dataclass(frozen=True, slots=True)
class Token:
    kind: str
    text: str


@dataclass(frozen=True, slots=True)
class Atom:
    symbol: str
    exponent: int = 1


@dataclass(frozen=True, slots=True)
class Group:
    expression: "Expression"
    exponent: int = 1


@dataclass(frozen=True, slots=True)
class Expression:
    numerator: tuple[Atom | Group, ...]
    denominator: tuple[Atom | Group, ...]


def normalize_unit_expression(expr: str) -> str:
    if not isinstance(expr, str):
        raise UnitSyntaxError("Unit expression must be a string")
    if any(char in _SUPERSCRIPTS for char in expr):
        raise UnitSyntaxError(
            f"Unicode superscript notation is not supported: {expr!r}. Use 'm^2'."
        )
    normalized = expr.strip().replace("\u00b5", "u").replace("\u03bc", "u")
    normalized = re.sub(r"\s+", "", normalized)
    if not normalized:
        raise UnitSyntaxError("Unit expression cannot be empty")
    return normalized


def tokenize_unit_expression(expr: str) -> list[Token]:
    expr = normalize_unit_expression(expr)
    tokens: list[Token] = []
    index = 0
    while index < len(expr):
        char = expr[index]
        if char.isalpha():
            match = _ATOM.match(expr, index)
            assert match
            atom = match.group()
            # A trailing integer remains the backwards-compatible compact
            # exponent (``m2``).  Digits inside a symbol are preserved for
            # catalogued engineering atoms such as ``mmH2O``.
            trailing_digits = re.search(r"\d+$", atom)
            if trailing_digits:
                tokens.append(Token("ATOM", atom[:trailing_digits.start()]))
                tokens.append(Token("INTEGER", trailing_digits.group()))
            else:
                tokens.append(Token("ATOM", atom))
            index = match.end()
        elif char.isdigit():
            end = index + 1
            while end < len(expr) and expr[end].isdigit():
                end += 1
            tokens.append(Token("INTEGER", expr[index:end]))
            index = end
        elif char in ".*":
            tokens.append(Token("MUL", char))
            index += 1
        elif char == "/":
            tokens.append(Token("DIV", char))
            index += 1
        elif char == "^":
            tokens.append(Token("POWER", char))
            index += 1
        elif char == "(":
            tokens.append(Token("LPAREN", char))
            index += 1
        elif char == ")":
            tokens.append(Token("RPAREN", char))
            index += 1
        elif char in "+-":
            tokens.append(Token("SIGN", char))
            index += 1
        else:
            raise UnitSyntaxError(f"Unexpected character {char!r} in unit expression {expr!r}")
    tokens.append(Token("EOF", ""))
    return tokens


class _Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = 0

    @property
    def current(self) -> Token:
        return self.tokens[self.index]

    def advance(self) -> Token:
        token = self.current
        self.index += 1
        return token

    def parse(self) -> Expression:
        expression = self.parse_expression()
        if self.current.kind != "EOF":
            raise UnitSyntaxError(f"Unexpected token {self.current.text!r}")
        return expression

    def parse_expression(self) -> Expression:
        numerator = [self.parse_factor()]
        while self.current.kind == "MUL":
            self.advance()
            numerator.append(self.parse_factor())
        denominator: list[Atom | Group] = []
        if self.current.kind == "DIV":
            self.advance()
            denominator.append(self.parse_factor())
            # Engineering convention: after '/', all same-level factors divide.
            while self.current.kind in {"MUL", "DIV"}:
                self.advance()
                denominator.append(self.parse_factor())
        return Expression(tuple(numerator), tuple(denominator))

    def parse_factor(self) -> Atom | Group:
        if self.current.kind == "ATOM":
            primary: Atom | Group = Atom(self.advance().text)
        elif self.current.kind == "INTEGER" and self.current.text == "1":
            primary = Atom("1")
            self.advance()
        elif self.current.kind == "LPAREN":
            self.advance()
            if self.current.kind == "RPAREN":
                raise UnitSyntaxError("Empty parentheses are not allowed")
            expression = self.parse_expression()
            if self.current.kind != "RPAREN":
                raise UnitSyntaxError("Unbalanced parentheses in unit expression")
            self.advance()
            primary = Group(expression)
        else:
            raise UnitSyntaxError(f"Expected a unit factor, got {self.current.text!r}")
        exponent = self.parse_exponent()
        if exponent == 1:
            return primary
        if isinstance(primary, Atom):
            return Atom(primary.symbol, exponent)
        return Group(primary.expression, exponent)

    def parse_exponent(self) -> int:
        caret = self.current.kind == "POWER"
        if caret:
            self.advance()
        elif self.current.kind != "INTEGER" and self.current.kind != "SIGN":
            return 1
        sign = 1
        if self.current.kind == "SIGN":
            sign = -1 if self.advance().text == "-" else 1
        if self.current.kind != "INTEGER":
            raise UnitSyntaxError("An exponent must be a signed integer")
        return sign * int(self.advance().text)


def parse_unit_expression(expr: str) -> Expression:
    return _Parser(tokenize_unit_expression(expr)).parse()
