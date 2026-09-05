"""Errors raised by the dimensional unit-conversion API."""


class UnitConversionError(ValueError):
    """Base class for dimensional conversion errors."""


class UnitSyntaxError(UnitConversionError):
    """The unit expression is not valid syntax."""


class UnknownUnitError(UnitConversionError):
    """A unit atom is not present in the registry."""


class DimensionMismatchError(UnitConversionError):
    """Two valid unit expressions have incompatible dimensions."""


class AffineUnitError(UnitConversionError):
    """An absolute affine unit was supplied to a multiplicative conversion."""


class CyclicUnitDefinitionError(UnitConversionError):
    """A recursive unit definition contains a cycle."""
