# 🔁 Legacy conversion

The original PyCUC converter uses named categories in `Refs`, including
pressure, temperature, density, energy, heat capacity, flow rate, and more.

```python
import pycuc

pycuc.convert_from_to(1, "MPa", "Pa")
pycuc.convert_from_to(1, "kg/m3", "g/cm3")
pycuc.convert_from_to(1, "W/m2.K", "BTU/(hr.ft2.F)")
```

## 🧱 Conversion blocks

```python
pycuc.to(125, "MPa => Pa")
pycuc.to(25, "C => K")
```

## 🌡️ Absolute temperature

Absolute temperatures have offsets, so use this API rather than `from_to()`.

```python
pycuc.convert_from_to(25, "C", "K")   # 298.15
pycuc.convert_from_to(32, "F", "C")   # 0.0
```

Use explicit interval units such as `dC` and `dF` in dimensional formulas.
