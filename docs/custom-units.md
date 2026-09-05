# 🧩 Custom units

Load controlled project-specific conversion tables from YAML.

```yaml
CUSTOM-UNIT:
  HEAT-CAPACITY:
    J/mol.K: 1
    kJ/mol.K: 0.001
    J/kmol.K: 1000
  ENERGY:
    J/mol: 1
    kJ/mol: 0.001
    kcal/mol: 0.000239006
```

```python
import pycuc

converter = pycuc.go("path/to/custom-unit.yml")
converter.from_to(1, "J/mol", "kJ/mol", reference="ENERGY")
```

For an in-memory table:

```python
converter = pycuc.create_cuc(25, "J/mol.K")
converter.add_custom_unit("J/mol.K", 1)
converter.add_custom_unit("kJ/mol.K", 1000)
converter.convert("kJ/mol.K")
```

Custom tables are category-based; use `pycuc.from_to()` for dimensional
algebra across supported `RefsX` units.
