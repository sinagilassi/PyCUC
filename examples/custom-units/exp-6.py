"""Basic dimensional conversions with the independent RefsX catalog."""

import pycuc
import sys
from pathlib import Path
from rich import print

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def main() -> None:
    examples = (
        # Molarity / amount concentration
        (1.0, "mol/L", "mol/m3"),
        (1.0, "M", "mmol/L"),
        (1.0, "mmol/L", "mol/m3"),
        (1.0, "µmol/L", "mol/m3"),

        # Molality
        (1.0, "mol/kg", "mmol/kg"),
        (1.0, "molal", "mol/kg"),

        # Mass concentration
        (1.0, "g/L", "kg/m3"),
        (1.0, "mg/L", "g/m3"),
        (1.0, "µg/L", "mg/m3"),

        # Clinical / laboratory
        (1.0, "mg/dL", "g/L"),
        (1.0, "g/dL", "g/L"),
    )

    for value, from_unit, to_unit in examples:
        result = pycuc.from_to(value, from_unit, to_unit)
        print(f"{value:g} {from_unit} = {result:.12g} {to_unit}")


if __name__ == "__main__":
    main()
