# 🚀 Quick start

```bash
pip install pycuc
```

## 📐 Equation-derived or compound units

Use `from_to()` for general dimensional expressions.  It validates SI
dimensions before converting.

```python
import pycuc

pycuc.from_to(1, "kg.m/s^2", "N")
pycuc.from_to(1, "kg.m^2/s^3", "W")
pycuc.from_to(1, "Pa.s", "cP")
```

## 🔁 Existing category units and absolute temperature

Use `convert_from_to()` for fixed legacy categories.  This is also the API
for absolute Celsius, Fahrenheit, Kelvin, and Rankine values.

```python
pycuc.convert_from_to(1, "MPa", "bar")
pycuc.convert_from_to(25, "C", "K")
pycuc.to(25, "C => K")
```

## 🧩 Project-specific units

Load a YAML conversion table with `pycuc.go("units.yml")`.  See
[Custom units](custom-units.md).
