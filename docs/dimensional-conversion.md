# 📐 Dimensional conversion

`pycuc.from_to(value, from_unit, to_unit)` converts compatible
multiplicative unit expressions.  It recursively reduces every unit atom
through the independent `RefsX` catalog to SI base dimensions, validates both
expressions, and converts using their SI factor ratio.

```python
import pycuc

pycuc.from_to(1, "kg.m/s^2", "N")            # 1.0
pycuc.from_to(1, "kg/(m.s^2)", "Pa")         # 1.0
pycuc.from_to(1, "kg.m^2/s^3", "W")          # 1.0
pycuc.from_to(1, "Pa.s", "mPa.s")            # 1000.0
```

## 🏭 Engineering examples

```python
# `.` and `*` are equivalent multiplication operators.
pycuc.from_to(1, "kJ/(mol.K)", "J/(mol*K)")
# 1000.0

# Repeated division follows engineering denominator semantics.
pycuc.from_to(1, "BTU/hr/ft^2/F", "W/m^2/K")
# 5.67826334111...

pycuc.from_to(1, "torr", "Pa")               # 133.322368421...
pycuc.from_to(1, "erg", "J")                 # 1e-7
pycuc.from_to(1, "cP", "Pa.s")               # 0.001
pycuc.from_to(1, "St", "m^2/s")              # 0.0001
pycuc.from_to(1, "hp", "W")                  # 745.699871582...
```

At an expression level, every factor after the first `/` belongs to the
denominator.  Therefore `kg/m/s^2` means `kg/(m.s^2)`.  Use parentheses when
you want explicit grouping:

```python
pycuc.from_to(1, "(m/s)^2", "m^2/s^2")
```

The parser accepts integer powers with `^` (`m^2`, `s^-2`) and legacy compact
powers (`m2`, `s-2`).  It accepts balanced parentheses.  Unicode superscript
notation is intentionally rejected; write `m^2`.

## 🧪 Concentrations

Symbols are case-sensitive:

```python
pycuc.from_to(1, "M", "mol/L")          # molar concentration
pycuc.from_to(1, "ML", "mol/kg")        # molal concentration
pycuc.from_to(1, "molality", "mol/kg")
```

`m` always means metre; it is not overloaded as molality.

## 🌡️ Temperature

`from_to()` is multiplicative and deliberately rejects standalone absolute
`C`, `F`, and `R` conversions, since they need offsets.  Use the existing
temperature API for absolute values:

```python
pycuc.convert_from_to(25, "C", "K")  # 298.15
```

Use explicit temperature-interval units for differences:

```python
pycuc.from_to(1, "dC", "dK")  # 1.0
pycuc.from_to(1, "dF", "dC")  # 0.555555...
```

Inside a compound expression, `C`, `F`, and `R` are interpreted as temperature
intervals.  This is why `BTU/(hr.ft^2.F)` is valid.

## 🛡️ Blind conversion rules

Use `from_to()` without a quantity category only when all of these are true:

1. Each unit is defined by `RefsX`, an accepted alias, or a valid SI prefix.
2. Both expressions obey the strict grammar.
3. They reduce to the same SI dimension vector.
4. The conversion is purely multiplicative; it does not require density,
   composition, reference conditions, or another material property.
5. You explicitly choose the target unit.  Dimensions alone do not decide
   semantics: `J` and `N.m` have the same dimensions but may mean energy or
   torque.

The API raises `UnitSyntaxError`, `UnknownUnitError`,
`DimensionMismatchError`, or `AffineUnitError` instead of guessing.

`ppm` is dimensionless, so `ppm -> mg/L` is not a blind conversion: it needs a
density assumption.  Apply that assumption in your own calculation.

## ⚡ Runnable examples

The repository includes these examples in `examples/custom-units/`:

- `exp-1.py` — core expressions.
- `exp-2.py` — process-engineering and legacy-compatible units.
- `exp-3.py` — warm-cache performance benchmark.
- `exp-4.py` — diverse-unit benchmark and catalog assessment.

Run one from the project root:

```powershell
python examples/custom-units/exp-4.py
```
