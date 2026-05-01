# 🔄 Python Custom Unit Converter (PyCUC)

![PyCUC Logo](./static/PyCUC-3.png)

![Downloads](https://img.shields.io/pypi/dm/PyCUC)
![PyPI](https://img.shields.io/pypi/v/PyCUC)
![Python Version](https://img.shields.io/pypi/pyversions/PyCUC.svg)
![License](https://img.shields.io/pypi/l/PyCUC)
![Read the Docs](https://img.shields.io/readthedocs/pycuc)

Python Custom Unit Converter (PyCUC) is an open-source package designed to simplify unit conversions in Python. With PyCUC, you can effortlessly create custom conversion factors, convert between units, and streamline calculations in various fields, such as physics, engineering, and scientific computing.

## ✨ Key Features

* 📐 **Custom Conversion Factors**: Define your own conversion factors for unique units
* 🔄 **Flexible Unit Conversions**: Convert between units with ease, using simple and intuitive methods
* 🪶 **Lightweight**: Minimal dependencies and optimized for performance
* 🚀 **Easy to Use**: Simple installation and straightforward usage

## References

PyCUC supports a wide range of unit conversions. Below are the updated references you can use for conversions:

- **Pressure**: Convert between units like bar, Pa, kPa, MPa, atm, mmHg, psi, etc.
- **Temperature**: Convert between units like C, F, K, R.
- **Density**: Convert between units like g/cm3, kg/L, kg/m3, lb/ft3, mol/L, kmol/m3, etc.
- **Concentration**: Convert between units like mol/m3, mol/L, M, mM, uM, nM, etc.
- **Energy**: Convert between units like J, kJ, cal, kcal, Wh, kWh, BTU, ft-lb, etc.
- **Energy Rate**: Convert between units like W, kW, MW, HP, BTU/s, BTU/min, BTU/h, cal/s, etc.
- **Gibbs Free Energy**: Convert between units like J/mol, kJ/mol, J/kmol, cal/mol, kcal/mol, J/kg, etc.
- **Enthalpy**: Convert between units like J/mol, kJ/mol, J/kmol, cal/mol, kcal/mol, J/kg, etc.
- **Heat Capacity**: Convert between units like J/kg.K, kJ/kg.K, cal/kg.K, BTU/lb.F, J/mol.K, kJ/mol.K, etc.
- **Heat Transfer Coefficient**: Convert between units like W/m2.K, kW/m2.K, W/cm2.K, W/ft2.K, BTU/(hr.ft2.F), etc.
- **Volume**: Convert between units like m3, L, cm3, dm3, ft3, in3, gal(US), gal(UK), etc.
- **Mass**: Convert between units like kg, g, mg, lb, oz, t, st, etc.
- **Molecular Weight**: Convert between units like g/mol, kg/kmol, lb/lbmol, kg/mol, mg/mol, g/kmol, etc.
- **Power**: Convert between units like W, kW, MW, GW, HP, BTU/h, ft-lb/min, etc.
- **Length**: Convert between units like m, cm, mm, km, ft, in, yd, mi, etc.
- **Area**: Convert between units like m2, cm2, mm2, km2, ft2, in2, yd2, hectare, acre, etc.
- **Force**: Convert between units like N, kN, lbf, kgf, dyn, ozf, etc.
- **Viscosity**: Convert between units like P, cP, Pa.s, mPa.s, g/cm.s, N.s/m2, lb/ft.s, etc.
- **Flow Rate**: Convert between units like mol/s, kmol/h, kg/s, g/min, m3/s, L/min, ft3/min, gal/min, bbl/day, etc.
- **Velocity**: Convert between units like m/s, cm/s, mm/s, km/h, ft/s, ft/min, in/s, mph, knot, etc.

## 📊 Google Colab

You can use the following code to run `PyCUC` in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AbTCZxz9xH0VxKCh-Qhb66X0GAGo9_0y?usp=sharing)


## 📥 Installation

Install PyCUC with pip:

```python
import pycuc
# check version
print(pycuc.__version__)
```


## 🔍 Usage Examples

### 📋 Example 1: Basic Operations

#### 🔍 Check References

```python
print(pycuc.check_reference('pressure'))
```

#### 🛠️ Create a Custom Unit Converter

```python
# ! pressure
my_cuc_1 = pycuc.create_cuc(1, 'MPa')
# convert to Pa
print(my_cuc_1.convert('Pa'))
print(my_cuc_1.convert('bar'))
print(my_cuc_1.convert('kPa'))

# ! temperature
my_cuc_2 = pycuc.create_cuc(358, 'K')
# convert to K
print(my_cuc_2.convert('C'))
print(my_cuc_2.convert('F'))
print(my_cuc_2.convert('R'))
```

#### ↔️ Convert From/To

```python
# ! pressure
print(pycuc.convert_from_to(1, 'MPa', 'Pa'))
# ! temperature
print(pycuc.convert_from_to(358, 'K', 'C'))
print(pycuc.convert_from_to(25, 'C', 'K'))
```

#### 🔄 Convert From/To (Short Format)

```python
# ! pressure
print(pycuc.to(125, 'MPa => Pa'))
# ! temperature
print(pycuc.to(360, 'K => C'))
print(pycuc.to(250, 'C => K'))
```


#### ✏️ Define a New Unit

```python
# ! heat capacity unit: J/mol.K
my_cuc_3 = pycuc.create_cuc(25, 'J/mol.K')
# add custom
my_cuc_3.add_custom_unit('J/mol.K', 1)
my_cuc_3.add_custom_unit('kJ/mol.K', 1000)
# conversion
print(my_cuc_3.convert('J/mol.K'))
print(my_cuc_3.convert('kJ/mol.K'))
```

#### 📚 Check Reference

```python
# ! pressure
print(my_cuc_3.check_reference('pressure'))
# ! temperature
print(my_cuc_3.check_reference('temperature'))
# ! custom
print(my_cuc_3.check_reference('custom'))
```


### 📋 Example 2: Advanced Usage


#### 📂 Load Custom Units from YML Files

```python
# load unit yml file
unit_file = os.path.join(os.getcwd(), 'test', 'custom-unit.yml')
my_cuc = pycuc.go(reference_file=unit_file)
```

#### 🔀 Using from_to Method

```python
# ! pressure
print(my_cuc.from_to(1, 'MPa', 'Pa'))
```

#### 🚀 Using to Method

```python
# ! pressure
print(my_cuc.to(125, 'MPa => Pa'))
```

#### 📋 Check References

```python
# ! from yml file
print(my_cuc.check_reference('custom::CUSTOM'))
print(my_cuc.check_reference('custom::HEAT-CAPACITY'))
print(my_cuc.check_reference('custom::ENERGY'))
```

## ❓ FAQ

For any questions, contact me on [LinkedIn](https://www.linkedin.com/in/sina-gilassi/)

## 👨‍💻 Authors

* [@sinagilassi](https://www.github.com/sinagilassi)
