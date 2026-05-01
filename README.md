# 🔄 Python Custom Unit Converter (PyCUC)

![PyCUC Logo](./static/PyCUC-3.png)

![Downloads](https://img.shields.io/pypi/dm/PyCUC) ![PyPI](https://img.shields.io/pypi/v/PyCUC) ![Python Version](https://img.shields.io/pypi/pyversions/PyCUC.svg) ![License](https://img.shields.io/pypi/l/PyCUC) ![Read the Docs](https://img.shields.io/readthedocs/pycuc)

Python Custom Unit Converter (PyCUC) is an open-source package designed to simplify unit conversions in Python. With PyCUC, you can effortlessly create custom conversion factors, convert between units, and streamline calculations in various fields, such as physics, engineering, and scientific computing.

## ✨ Key Features

* 📐 **Custom Conversion Factors**: Define your own conversion factors for unique units
* 🔄 **Flexible Unit Conversions**: Convert between units with ease, using simple and intuitive methods
* 🪶 **Lightweight**: Minimal dependencies and optimized for performance
* 🚀 **Easy to Use**: Simple installation and straightforward usage

## References

PyCUC supports a wide range of unit conversions. Below are the updated references you can use for conversions:

- **Density**: Convert between units like kg/m³, g/cm³, lb/ft³, etc.
- **Energy**: Convert between units like J, kJ, cal, BTU, etc.
- **Heat Capacity**: Convert between units like J/mol·K, kJ/mol·K, cal/mol·K, etc.
- **Volume**: Convert between units like m³, L, mL, ft³, etc.
- **Mass**: Convert between units like kg, g, lb, oz, etc.
- **Power**: Convert between units like W, kW, HP, etc.
- **Length**: Convert between units like m, cm, mm, in, ft, etc.
- **Force**: Convert between units like N, kN, lbf, etc.
- **Velocity**: Convert between units like m/s, km/h, ft/s, mph, knots, etc.

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
