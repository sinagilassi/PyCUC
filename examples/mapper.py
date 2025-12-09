# import packages/modules
from rich import print
from typing import Dict, Any
# local
import pycuc
from pycuc.utils.tools import map_to_reference


# check version
print(pycuc.__version__)

# =====================================
# SECTION: CHECK REFERENCES
# =====================================
# check references
print(pycuc.check_reference('PRESSURE'))

# check reference units
print(pycuc.all_units('PRESSURE'))

# check all reference units
print(pycuc.all_units())

# check unit availability
print(pycuc.is_unit_available('bar', 'PRESSURE'))
print(pycuc.is_unit_available('C', 'TEMPERATURE'))
print(pycuc.is_unit_available('kg/m3'))

# =====================================
# SECTION: MAPPER
# =====================================
# inputs
inputs: Dict[str, Any] = {
    'Tc': {
        'value': 0,
        'unit': 'K',
        'symbol': 'Tc'
    },
    'T': {
        'value': None,
        'unit': 'K',
        'symbol': 'T'
    }
}

# reference
reference: Dict[str, Any] = {
    'Tc': {
        'name': 'critical temperature',
        'symbol': 'Tc',
        'unit': 'C'
    },
    'T': {
        'name': 'temperature',
        'symbol': 'T',
        'unit': 'F0'
    }
}

# map
print(map_to_reference(
    inputs=inputs,
    reference=reference,
    verbose=True
))
