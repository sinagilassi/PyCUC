# REFERENCE CLASS
# ================

# import module/packages
from typing import Dict, List


# local

class Refs:

    # vars
    # SECTION: Pressure Conversions
    _pressure_conversions_ref: Dict[str, float] = {
        'bar': 1.0,
        'mbar': 1000.0,
        'ubar': 1000000.0,
        'Pa': 100000.0,
        'hPa': 1000.0,
        'kPa': 100.0,
        'MPa': 0.1,
        'kg/cm2': 1.01972,
        'atm': 0.986923,
        'mmHg': 750.062,
        'mmH2O': 10197.162129779,
        'mH2O': 10.197162129779,
        'psi': 14.5038,
        'ftH2O': 33.455256555148,
        'inH2O': 401.865,
        'inHg': 29.53
    }

    # SECTION: Temperature Conversions
    _temperature_conversions_ref: Dict[str, float] = {
        'C': 0,  # Celsius
        'F': 32,  # Fahrenheit
        'K': -273.15,  # Kelvin
        'R': 491.67  # Rankine
    }

    # SECTION: Density Conversions
    _density_conversions_ref: Dict[str, float] = {
        # mass per volume
        'g/cm3': 1.0,  # ! base unit
        'kg/dm3': 1.0,
        't/m3': 1.0,
        'kg/m3': 1000.0,
        'lb/ft3': 62.42796,
        'lb/in3': 0.0361273,
        # mole per volume
        "kmol/m3": 1.0,  # ! base unit
        "mol/m3": 1000.0,
        "kmol/dm3": 0.001,
        "mol/dm3": 1.0,
        "kmol/cm3": 1e-6,
        "mol/cm3": 0.001,
        "mol/L": 1.0,
        "kmol/L": 0.001,
        "mol/ft3": 35.3147,
        "kmol/ft3": 0.0353147
    }

    # SECTION: Energy Conversions
    _energy_conversions_ref: Dict[str, float] = {
        'J': 1.0,
        'kJ': 0.001,
        'cal': 0.239006,
        'kcal': 0.000239006,
        'Wh': 0.000277778,
        'kWh': 2.77778e-7,
        'BTU': 0.000947817,
        'ft-lb': 0.737562
    }

    # SECTION: Gibbs Free Energy Conversions
    _gibbs_free_energy_conversions_ref: Dict[str, float] = {
        # per mol and kmol
        'J/mol': 1.0,
        'kJ/mol': 0.001,
        'J/kmol': 1000.0,
        'cal/mol': 0.239005736,
        'kcal/mol': 0.0002390057,
        'kcal/kmol': 0.2390057,
        'cal/kmol': 239.0057,
        # per kg and g
        'J/kg': 1.0,
        'kJ/kg': 0.001,
        'cal/g': 0.000239006,
        'kcal/g': 2.39006e-7,
        'J/g': 0.001,
        'kJ/g': 1.0e-6,
        'cal/kg': 0.239006,
        'kcal/kg': 0.000239006,
    }

    # SECTION: Enthalpy Conversions
    _enthalpy_conversions_ref: Dict[str, float] = {
        # per mol and kmol
        'J/mol': 1.0,
        'kJ/mol': 0.001,
        'J/kmol': 1000.0,
        'cal/mol': 0.239005736,
        'kcal/mol': 0.0002390057,
        'kcal/kmol': 0.2390057,
        'cal/kmol': 239.0057,
        # per kg and g
        'J/kg': 1.0,
        'kJ/kg': 0.001,
        'cal/g': 0.000239006,
        'kcal/g': 2.39006e-7,
        'J/g': 0.001,
        'kJ/g': 1.0e-6,
        'cal/kg': 0.239006,
        'kcal/kg': 0.000239006,
    }

    # SECTION: Heat capacity Conversions
    _heat_capacity_conversions_ref: Dict[str, float] = {
        # mass basis
        'J/kg.K': 1.0,
        'kJ/kg.K': 0.001,
        'cal/kg.K': 0.239006,
        'kcal/kg.K': 0.000239006,
        'cal/g.K': 0.000239006,
        'J/g.K': 0.001,
        'kJ/g.K': 1.0e-6,
        'BTU/lb.F': 0.000238846,
        # molar basis
        'J/mol.K': 1.0,
        'kJ/mol.K': 0.001,
        'cal/mol.K': 0.239005736,
        'kcal/mol.K': 0.0002390057,
        'cal/kmol.K': 239.0057,
        'kcal/kmol.K': 0.2390057,
        'J/kmol.K': 1000.0,
        'kJ/kmol.K': 1.0,
    }

    # SECTION: Volume Conversions
    _volume_conversions_ref: Dict[str, float] = {
        'm3': 1.0,
        'L': 1000.0,
        'cm3': 1000000.0,
        'dm3': 1000.0,
        'ft3': 35.3147,
        'in3': 61023.7,
        'gal(US)': 264.172,
        'gal(UK)': 219.969
    }

    # SECTION: Mass Conversions
    _mass_conversions_ref: Dict[str, float] = {
        'kg': 1.0,
        'g': 1000.0,
        'mg': 1000000.0,
        'lb': 2.20462,
        'oz': 35.274,
        't': 0.001,
        'st': 0.157473
    }

    # SECTION: Power Conversions
    _power_conversions_ref: Dict[str, float] = {
        'W': 1.0,
        'kW': 0.001,
        'MW': 1e-6,
        'GW': 1e-9,
        'HP': 0.00134102,
        'BTU/h': 3.41214,
        'ft-lb/min': 0.737562
    }

    # SECTION: Length Conversions
    _length_conversions_ref: Dict[str, float] = {
        'm': 1.0,
        'cm': 100.0,
        'mm': 1000.0,
        'km': 0.001,
        'ft': 3.28084,
        'in': 39.3701,
        'yd': 1.09361,
        'mi': 0.000621371
    }

    # SECTION: Force Conversions
    _force_conversions_ref: Dict[str, float] = {
        'N': 1.0,
        'kN': 0.001,
        'lbf': 0.224809,
        'kgf': 0.101972,
        'dyn': 100000,
        'ozf': 35.274
    }

    # SECTION: Viscosity Conversions
    _viscosity_conversions_ref: Dict[str, float] = {
        'P': 1.0,
        'cP': 100.0,
        'Pa.s': 0.1,
        'mPa.s': 100.0,
        'g/cm.s': 1.0,
        'N.s/m2': 0.1,
        'μP': 1e6,
        'lb/ft.s': 0.671968,
        'lb/ft.h': 241.908
    }

    # SECTION: Flow-rate Conversions
    _flow_rate_conversions_ref: Dict[str, float] = {
        # molar basis
        "mol/s": 1.0,
        "kmol/s": 0.001,
        "mol/min": 60.0,
        "kmol/min": 0.06,
        "mol/h": 3600.0,
        "kmol/h": 3.6,
        # mass basis
        "kg/s": 1.0,
        "g/s": 1000.0,
        "kg/min": 60.0,
        "g/min": 60000.0,
        "kg/h": 3600.0,
        "g/h": 3600000.0,
        # volume basis
        "m3/s": 1.0,
        "L/s": 1000.0,
        "l/s": 1000.0,
        "m3/min": 60.0,
        "L/min": 60000.0,
        "l/min": 60000.0,
        "m3/h": 3600.0,
        "L/h": 3600000.0,
        "l/h": 3600000.0,
        "mL/s": 1e6,
        "mL/min": 6e7,
        "mL/h": 3.6e9,
        "ft3/s": 35.3147,
        "ft3/min": 2118.88,
        "ft3/h": 127132.8
    }

    # SECTION: Reference
    _reference = {
        'PRESSURE': _pressure_conversions_ref,
        'TEMPERATURE': _temperature_conversions_ref,
        'DENSITY': _density_conversions_ref,
        'ENERGY': _energy_conversions_ref,
        'GIBBS_FREE_ENERGY': _gibbs_free_energy_conversions_ref,
        'ENTHALPY': _enthalpy_conversions_ref,
        'HEAT_CAPACITY': _heat_capacity_conversions_ref,
        'VOLUME': _volume_conversions_ref,
        'MASS': _mass_conversions_ref,
        'POWER': _power_conversions_ref,
        'LENGTH': _length_conversions_ref,
        'FORCE': _force_conversions_ref,
        'VISCOSITY': _viscosity_conversions_ref,
        'FLOW_RATE': _flow_rate_conversions_ref
    }

    def __init__(self):
        pass

    @property
    def pressure_conversions_ref(self):
        return self._pressure_conversions_ref

    @property
    def temperature_conversions_ref(self):
        return self._temperature_conversions_ref

    @property
    def density_conversions_ref(self):
        return self._density_conversions_ref

    @property
    def energy_conversions_ref(self):
        return self._energy_conversions_ref

    @property
    def gibbs_free_energy_conversions_ref(self):
        return self._gibbs_free_energy_conversions_ref

    @property
    def enthalpy_conversions_ref(self):
        return self._enthalpy_conversions_ref

    @property
    def heat_capacity_conversions_ref(self):
        return self._heat_capacity_conversions_ref

    @property
    def volume_conversions_ref(self):
        return self._volume_conversions_ref

    @property
    def mass_conversions_ref(self):
        return self._mass_conversions_ref

    @property
    def power_conversions_ref(self):
        return self._power_conversions_ref

    @property
    def length_conversions_ref(self):
        return self._length_conversions_ref

    @property
    def force_conversions_ref(self):
        return self._force_conversions_ref

    @property
    def viscosity_conversions_ref(self):
        return self._viscosity_conversions_ref

    @property
    def flow_rate_conversions_ref(self):
        return self._flow_rate_conversions_ref

    @staticmethod
    def get_reference():
        return Refs._reference

    @staticmethod
    def get_reference_by_key(key: str):
        reference = Refs.get_reference()
        return reference.get(key, None)

    @staticmethod
    def get_reference_units_by_key(key: str) -> List[str]:
        reference = Refs.get_reference()
        ref = reference.get(key, None)
        if ref is not None:
            return list(ref.keys())
        else:
            return []

    @staticmethod
    def get_all_reference_units() -> List[str]:
        reference = Refs.get_reference()
        all_units = []
        for key, ref in reference.items():
            all_units.extend(list(ref.keys()))
        return all_units

    @staticmethod
    def is_unit_in_reference(unit: str) -> bool:
        all_units = Refs.get_all_reference_units()
        # lowercase
        all_units = [u.lower() for u in all_units]
        unit = unit.lower()
        return unit in all_units

    @staticmethod
    def is_unit_in_reference_by_key(
        unit: str,
        key: str
    ) -> bool:
        units = Refs.get_reference_units_by_key(key)
        # lowercase
        units = [u.lower() for u in units]
        unit = unit.lower()
        return unit in units
