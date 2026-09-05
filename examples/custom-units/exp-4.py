"""Diverse unit-conversion benchmark for cached dimensional conversions.

Run this file from the repository root.  It reports a warm-cache average, so
the result measures normal repeated use rather than Python import time.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from time import perf_counter

import pycuc
from pycuc.docs.dimensional import resolve_unit_expression, validate_unit_registry
from rich import print


# ---------------------------------------------------------------------------
# Diverse conversion cases
# ---------------------------------------------------------------------------
CASES = (
    # --- Basic SI force / pressure / energy / power ---
    (1.0, "kg.m/s^2", "N"),
    (1.0, "kg/(m.s^2)", "Pa"),
    (1.0, "kg.m^2/s^3", "W"),
    (1.0, "kJ/(mol.K)", "J/(mol.K)"),
    (1.0, "Pa.s", "mPa.s"),

    # --- Process-engineering heat-transfer coefficients ---
    (1.0, "W/(m^2.K)", "BTU/(hr.ft^2.F)"),
    (1.0, "BTU/hr/ft^2/F", "W/m^2/K"),
    (1.0, "kcal/(h.m^2.C)", "W/(m^2.K)"),

    # --- Legacy / engineering pressure units ---
    (1.0, "inHg", "kPa"),
    (1.0, "mmH2O", "Pa"),
    (1.0, "kg/cm2", "bar"),
    (1.0, "kg/cm2", "psi"),
    (1.0, "atm", "kPa"),
    (1.0, "torr", "Pa"),
    (1.0, "psi", "bar"),

    # --- Flow rates ---
    (10.0, "gal(US)/min", "L/min"),
    (1.0, "m3/h", "gal(US)/min"),
    (1.0, "ft3/s", "m3/s"),
    (60.0, "mph", "m/s"),
    (1.0, "km/h", "m/s"),

    # --- Energy / work ---
    (1.0, "kWh", "J"),
    (1.0, "BTU", "J"),
    (1.0, "cal", "J"),
    (1.0, "kcal", "kJ"),
    (1.0, "erg", "J"),

    # --- Explicit temperature intervals; absolute temperatures use convert_from_to ---
    (1.0, "dK", "dC"),
    (1.0, "dF", "dC"),
    # (1.0, "R", "K"),          # Rankine ↔ Kelvin

    # --- Mass / molar concentrations & related ---
    (1.0, "g/L", "kg/m3"),
    (1.0, "mol/L", "mol/m3"),
    (1.0, "M", "mol/L"),
    (1.0, "ML", "mol/kg"),
    (1.0, "ppm", "ppb"),
    # ppm -> mg/L requires an explicit density assumption, so it is not blind.

    # --- Viscosity & related ---
    (1.0, "cP", "Pa.s"),
    (1.0, "P", "Pa.s"),
    (1.0, "St", "m2/s"),      # Stokes

    # --- Power / heat-rate ---
    (1.0, "hp", "W"),
    (1.0, "BTU/hr", "W"),
    (1.0, "kcal/h", "W"),

    # --- Length / area / volume mixed systems ---
    (1.0, "ft", "m"),
    (1.0, "in", "mm"),
    (1.0, "acre", "m2"),
    (1.0, "gal(US)", "L"),
    (1.0, "bbl", "m3"),       # oil barrel

    # --- Compound / nested expressions ---
    (1.0, "N.m", "J"),
    (1.0, "kg.m2/s2", "J"),
    (1.0, "W.s", "J"),
    (1.0, "Pa.m3", "J"),
)

ITERATIONS = 20_000


def main() -> None:
    validate_unit_registry()

    # Populate the expression-resolution cache before measuring steady state.
    for _, from_unit, to_unit in CASES:
        resolve_unit_expression(from_unit)
        resolve_unit_expression(to_unit)

    started = perf_counter()
    for _ in range(ITERATIONS):
        for value, from_unit, to_unit in CASES:
            pycuc.from_to(value, from_unit, to_unit)
    elapsed = perf_counter() - started

    conversions = ITERATIONS * len(CASES)
    print(f"Validated RefsX and executed {conversions:,} conversions "
          f"across {len(CASES)} diverse unit pairs.")
    print(f"Elapsed: {elapsed:.4f} s")
    print(
        f"Average: {elapsed / conversions * 1_000_000:.2f} microseconds/conversion")


if __name__ == "__main__":
    main()
