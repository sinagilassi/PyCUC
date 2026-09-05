"""Process-engineering and legacy-compatible dimensional conversions."""

import pycuc
import sys
from pathlib import Path
from rich import print

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def main() -> None:
    examples = (
        # Parenthesized and loose engineering denominator styles are equivalent.
        (1.0, "W/(m^2.K)", "BTU/(hr.ft^2.F)"),
        (1.0, "BTU/hr/ft^2/F", "W/m^2/K"),
        # RefsX supplies independent definitions for these legacy pressure units.
        (1.0, "inHg", "kPa"),
        (1.0, "mmH2O", "Pa"),
        (1.0, "kg/cm2", "bar"),
        (10.0, "gal(US)/min", "L/min"),
        (60.0, "mph", "m/s"),
    )

    for value, from_unit, to_unit in examples:
        result = pycuc.from_to(value, from_unit, to_unit)
        print(f"{value:g} {from_unit} = {result:.12g} {to_unit}")


if __name__ == "__main__":
    main()
