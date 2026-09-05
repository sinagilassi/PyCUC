# 🗂️ References and mapping

## 🔎 Explore the legacy catalog

```python
import pycuc

pycuc.check_reference("PRESSURE")
pycuc.all_units("PRESSURE")
pycuc.all_units()
pycuc.is_unit_available("bar", "PRESSURE")
```

## 🧭 Map input data to a schema

```python
from pycuc.utils.tools import map_to_reference

inputs = {"Tc": {"value": 0, "unit": "K", "symbol": "Tc"}}
reference = {
    "Tc": {"name": "critical temperature", "symbol": "Tc", "unit": "C"}
}

mapped = map_to_reference(inputs=inputs, reference=reference, verbose=True)
```

See `examples/mapper.py` for a complete runnable example.
