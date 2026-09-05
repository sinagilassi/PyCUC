"""Basic dimensional conversions with the independent RefsX catalog."""

import pycuc
import sys
from pathlib import Path
from rich import print

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def main() -> None:
    examples = (
        (1.0, "kg/(m.s^2)", "Pa"),
        (1.0, "kJ/mol.K", "J/mol.K"),
        (1.0, "kg.m^2/s^3", "W"),
        (1.0, "Pa.s", "mPa.s"),
        (100.0, "dC", "dF"),
        (1.0, "bar", "psi"),
        (1.0, "atm", "kPa"),
        (1.0, "kg/m3", "lb/ft3"),
        (1.0, "mol/L", "mol/m3"),
        (1.0, "kJ/mol", "cal/mol"),
        (1.0, "kW", "HP"),
        (1.0, "J/mol.K", "cal/mol.K"),
        (1.0, "W/m2.K", "BTU/(hr.ft2.F)"),
        (1.0, "m3", "gal(US)"),
        (1.0, "kg", "lb"),
        (1.0, "g/mol", "kg/kmol"),
        (1.0, "m", "ft"),
        (1.0, "m2", "ft2"),
        (1.0, "N", "lbf"),
        (1.0, "cP", "Pa.s"),
        (1.0, "mol/s", "kmol/h"),
        (1.0, "kg/s", "lb/s"),
        (1.0, "m3/h", "gal/min"),
        (1.0, "m/s", "mph"),
    )

    for value, from_unit, to_unit in examples:
        result = pycuc.from_to(value, from_unit, to_unit)
        print(f"{value:g} {from_unit} = {result:.12g} {to_unit}")


if __name__ == "__main__":
    main()
