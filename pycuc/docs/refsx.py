"""Self-contained reference catalog for dimensional conversions.

``RefsX`` deliberately does not import or depend on the legacy ``Refs``
tables.  Each entry supplies a physical reduction to SI base units.
"""


class RefsX:
    _prefixes_ref = {
        "Q": 30, "R": 27, "Y": 24, "Z": 21, "E": 18, "P": 15,
        "T": 12, "G": 9, "M": 6, "k": 3, "h": 2, "da": 1,
        "d": -1, "c": -2, "m": -3, "u": -6, "n": -9, "p": -12,
        "f": -15, "a": -18, "z": -21, "y": -24, "r": -27, "q": -30,
    }

    # mass, length, time, current, temperature, amount, luminous intensity
    _unit_definitions_ref = {
        "kg": {"dimension": (1, 0, 0, 0, 0, 0, 0)},
        "m": {"dimension": (0, 1, 0, 0, 0, 0, 0), "prefixable": True},
        "s": {"dimension": (0, 0, 1, 0, 0, 0, 0), "prefixable": True, "aliases": ("sec",)},
        "A": {"dimension": (0, 0, 0, 1, 0, 0, 0), "prefixable": True},
        "K": {"dimension": (0, 0, 0, 0, 1, 0, 0), "prefixable": True},
        "mol": {"dimension": (0, 0, 0, 0, 0, 1, 0), "prefixable": True},
        "cd": {"dimension": (0, 0, 0, 0, 0, 0, 1), "prefixable": True},
        "C": {"dimension": (0, 0, 0, 0, 1, 0, 0), "interval_scale": 1.0},
        "F": {"dimension": (0, 0, 0, 0, 1, 0, 0), "interval_scale": 5 / 9},
        "R": {"dimension": (0, 0, 0, 0, 1, 0, 0), "interval_scale": 5 / 9},
        # Explicit temperature intervals avoid ambiguity with absolute C/F/R.
        "dK": {"dimension": (0, 0, 0, 0, 1, 0, 0)},
        "dC": {"dimension": (0, 0, 0, 0, 1, 0, 0)},
        "dF": {"dimension": (0, 0, 0, 0, 1, 0, 0), "scale": 5 / 9},
        "dR": {"dimension": (0, 0, 0, 0, 1, 0, 0), "scale": 5 / 9},
        "Hz": {"definition": "1/s", "prefixable": True},
        "N": {"definition": "kg.m/s^2", "prefixable": True},
        "Pa": {"definition": "N/m^2", "prefixable": True},
        "J": {"definition": "N.m", "prefixable": True},
        "W": {"definition": "J/s", "prefixable": True},
        "g": {"definition": "kg", "scale": 0.001, "prefixable": True},
        "microgram": {"definition": "kg", "scale": 1e-9},
        "lb": {"definition": "kg", "scale": 0.45359237, "aliases": ("lbm",)},
        "oz": {"definition": "kg", "scale": 0.028349523125},
        "tonne": {"definition": "kg", "scale": 1000, "aliases": ("t",)},
        "st": {"definition": "kg", "scale": 6.35029318},
        "slug": {"definition": "kg", "scale": 14.5939029372},
        "in": {"definition": "m", "scale": 0.0254},
        "ft": {"definition": "m", "scale": 0.3048},
        "yd": {"definition": "m", "scale": 0.9144},
        "mile": {"definition": "m", "scale": 1609.344, "aliases": ("mi",)},
        "angstrom": {"definition": "m", "scale": 1e-10, "aliases": ("Angstrom",)},
        "micron": {"definition": "m", "scale": 1e-6},
        "min": {"definition": "s", "scale": 60},
        "hr": {"definition": "s", "scale": 3600, "aliases": ("hour", "h")},
        "day": {"definition": "s", "scale": 86400},
        "L": {"definition": "m^3", "scale": 0.001, "prefixable": True, "aliases": ("l",)},
        "microliter": {"definition": "m^3", "scale": 1e-9, "aliases": ("microlitre",)},
        "galUS": {"definition": "m^3", "scale": 0.003785411784, "aliases": ("gal",)},
        "galUK": {"definition": "m^3", "scale": 0.00454609},
        "bbl": {"definition": "m^3", "scale": 0.158987294928, "aliases": ("barrel",)},
        "ha": {"definition": "m^2", "scale": 10000, "aliases": ("hectare",)},
        "acre": {"definition": "m^2", "scale": 4046.8564224},
        "bar": {"definition": "Pa", "scale": 100000, "prefixable": True},
        "atm": {"definition": "Pa", "scale": 101325},
        "psi": {"definition": "Pa", "scale": 6894.757293168},
        "mmHg": {"definition": "Pa", "scale": 133.322387415},
        "torr": {"definition": "Pa", "scale": 101325 / 760},
        "inHg": {"definition": "Pa", "scale": 3386.38815789},
        "mmH2O": {"definition": "Pa", "scale": 9.80665},
        "mH2O": {"definition": "Pa", "scale": 9806.65},
        "ftH2O": {"definition": "Pa", "scale": 2989.06692},
        "inH2O": {"definition": "Pa", "scale": 249.08891},
        "lbf": {"definition": "N", "scale": 4.4482216152605},
        "kgf": {"definition": "N", "scale": 9.80665},
        "ozf": {"definition": "N", "scale": 0.278013850953781},
        "dyn": {"definition": "N", "scale": 1e-5},
        "cal": {"definition": "J", "scale": 4.184, "prefixable": True},
        "erg": {"definition": "J", "scale": 1e-7},
        "BTU": {"definition": "J", "scale": 1055.05585262},
        "Wh": {"definition": "W.hr", "prefixable": True},
        "HP": {"definition": "W", "scale": 745.69987158227, "aliases": ("hp",)},
        "P": {"definition": "Pa.s", "scale": 0.1, "prefixable": True},
        "St": {"definition": "m^2/s", "scale": 1e-4, "prefixable": True},
        "knot": {"definition": "m/s", "scale": 0.514444444444444, "aliases": ("kn",)},
        "lbmol": {"definition": "mol", "scale": 453.59237},
        "M": {"definition": "mol/L", "prefixable": True, "aliases": ("molar",)},
        "ML": {"definition": "mol/kg", "aliases": ("molal", "molality")},
        "sg": {"definition": "1"},
        "ppm": {"definition": "1", "scale": 1e-6},
        "ppb": {"definition": "1", "scale": 1e-9},
        "mph": {"definition": "mile/hr"},
    }

    # Backward-compatible legacy spellings which cannot be represented by the
    # strict grammar as individual atoms.  Values remain dimensional formulas.
    _expression_aliases_ref = {
        "kg/cm2": "kgf/cm^2",
        "gal(US)": "galUS",
        "gal(UK)": "galUK",
        "ft-lb": "ft.lbf",
        "ft-lb/min": "ft.lbf/min",
    }
