"""Small, repeatable benchmark for cached dimensional conversions.

Run this file from the repository root.  It reports a warm-cache average, so
the result measures normal repeated use rather than Python import time.
"""

from pycuc.docs.dimensional import resolve_unit_expression, validate_unit_registry
import pycuc
from time import perf_counter
import sys
from pathlib import Path
from rich import print

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


CASES = (
    (1.0, "kg.m/s^2", "N"),
    (1.0, "kJ/(mol.K)", "J/(mol.K)"),
    (1.0, "W/(m^2.K)", "BTU/(hr.ft^2.F)"),
    (1.0, "BTU/hr/ft^2/F", "W/m^2/K"),
    (1.0, "kg/cm2", "psi"),
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
    print(f"Validated RefsX and executed {conversions:,} conversions.")
    print(f"Elapsed: {elapsed:.4f} s")
    print(
        f"Average: {elapsed / conversions * 1_000_000:.2f} microseconds/conversion")


if __name__ == "__main__":
    main()
