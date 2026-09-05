"""Basic dimensional conversions with the independent RefsX catalog."""

import pycuc
import sys
from pathlib import Path
from rich import print

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def main() -> None:
    examples = (
        (1.0, "kg.m/s^2", "N"),
        (1.0, "kg/(m.s^2)", "Pa"),
        (1.0, "kJ/(mol.K)", "J/(mol.K)"),
        (1.0, "kg.m^2/s^3", "W"),
        (1.0, "Pa.s", "mPa.s"),
    )

    for value, from_unit, to_unit in examples:
        result = pycuc.from_to(value, from_unit, to_unit)
        print(f"{value:g} {from_unit} = {result:.12g} {to_unit}")


if __name__ == "__main__":
    main()
