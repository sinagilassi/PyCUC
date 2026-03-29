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
        'kg/cm²': 1.01972,  # with unicode
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
        'g/cm³': 1.0,  # ! base unit with unicode
        'kg/L': 1.0,
        'g/m3': 1000000,
        'g/m³': 1000000,  # with unicode
        'kg/dL': 10.0,
        'g/L': 0.001,
        'g/l': 0.001,
        'g/mL': 1.0,
        'g/ml': 1.0,
        'kg/dm3': 1.0,
        'kg/dm³': 1.0,  # with unicode
        't/m3': 1.0,
        't/m³': 1.0,  # with unicode
        'tonne/m3': 1.0,
        'tonne/m³': 1.0,  # with unicode
        'kg/m3': 1000.0,
        'kg/m³': 1000.0,  # with unicode
        'lb/ft3': 62.42796,
        'lb/ft³': 62.42796,  # with unicode
        'lb/in3': 27.6799,
        'lb/in³': 27.6799,  # with unicode
        # Optional common additions
        # specific gravity (dimensionless, relative to water at 1 g/cm³)
        'sg': 1.0,
        'oz/gal': 133.526,       # US oz/gal (fluid) to g/cm³ — if needed later
        # mole per volume
        "kmol/m3": 1.0,  # ! base unit
        "kmol/m³": 1.0,  # ! base unit with unicode
        "mol/m3": 1000.0,
        "mol/m³": 1000.0,  # with unicode
        "kmol/dm3": 0.001,
        "kmol/dm³": 0.001,  # with unicode
        "mol/dm3": 1.0,
        "mol/dm³": 1.0,  # with unicode
        "kmol/cm3": 1e-6,
        "kmol/cm³": 1e-6,  # with unicode
        "mol/cm3": 0.001,
        "mol/cm³": 0.001,  # with unicode
        "mol/L": 1.0,
        "mol/l": 1.0,
        "M": 1.0,  # molarity shorthand
        "kmol/L": 0.001,
        "kmol/l": 0.001,
        "mol/ft3": 28.3168466,
        "mol/ft³": 28.3168466,  # with unicode
        "kmol/ft3": 0.0283168466,
        "kmol/ft³": 0.0283168466,  # with unicode
    }

    # SECTION: Concentration Conversions (mole based)
    _concentration_conversions_ref: Dict[str, float] = {
        # NOTE: base is mol/m3
        'mol/m3': 1.0,   # ! base unit
        'mol/m\u00B3': 1.0,   # ! base unit with unicode
        # mol/XXX forms
        'mol/cm3': 1.0e-6,
        'mol/cm\u00B3': 1.0e-6,  # with unicode
        'mol/dm3': 0.001,
        'mol/dm\u00B3': 0.001,   # with unicode
        'mol/L': 0.001,
        'mol/l': 0.001,
        'mol/mL': 1.0e-6,
        'mol/ml': 1.0e-6,
        'mol/ft3': 0.0283168466,
        'mol/ft\u00B3': 0.0283168466,  # with unicode
        # kmol basis
        'kmol/m3': 0.001,
        'kmol/m\u00B3': 0.001,  # with unicode
        # molarity shorthand
        'M': 0.001,
        'mM': 1.0,
        'uM': 1000.0,
        '\u03BCM': 1000.0,  # Greek mu
        '\u00B5M': 1000.0,  # micro sign
        'nM': 1.0e6,
        'pM': 1.0e9
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

    _heat_transfer_coefficient_ref: Dict[str, float] = {
        # base
        'W/m2.K': 1.0,
        'W/m².K': 1.0,
        'W/m2K': 1.0,
        'W/m²K': 1.0,

        # SI scaled
        'kW/m2.K': 0.001,
        'kW/m².K': 0.001,

        # area variations
        'W/cm2.K': 1.0e-4,
        'W/cm².K': 1.0e-4,
        'W/mm2.K': 1.0e-6,
        'W/mm².K': 1.0e-6,
        'W/ft2.K': 0.092903,
        'W/ft².K': 0.092903,

        # imperial
        'BTU/(hr.ft2.F)': 0.1761101838,
        'BTU/(hr.ft².F)': 0.1761101838,
        'BTU/hr.ft2.F': 0.1761101838,

        # thermal engineering
        'kcal/(hr.m2.K)': 0.859845,
        'kcal/(hr.m².K)': 0.859845,
    }

    # SECTION: Volume Conversions
    _volume_conversions_ref: Dict[str, float] = {
        'm3': 1.0,
        'm³': 1.0,          # if you want Unicode
        'L': 1000.0,
        'cm3': 1000000.0,
        'cm³': 1000000.0,  # if you want Unicode
        'dm3': 1000.0,
        'dm³': 1000.0,  # if you want Unicode
        'ft3': 35.3147,
        'ft³': 35.3147,  # if you want Unicode
        'in3': 61023.7,
        'in³': 61023.7,  # if you want Unicode
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

    # SECTION: Molecular Weight Conversions
    _molecular_weight_conversions_ref: Dict[str, float] = {
        # NOTE: base is g/mol
        'g/mol': 1.0,        # ! base unit

        # Same numerical value
        'kg/kmol': 1.0,
        'lb/lbmol': 1.0,

        # Larger unit (value decreases)
        'kg/mol': 0.001,     # 1 g/mol = 0.001 kg/mol

        # Smaller units (value increases)
        'mg/mol': 1000.0,    # 1 g/mol = 1000 mg/mol
        'g/kmol': 1000.0,    # 1 g/mol = 1000 g/kmol

        # Imperial mass per mole
        'lb/mol': 0.00220462,   # 1 g/mol = 0.00220462 lb/mol
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

    # SECTION: Area Conversions
    _area_conversions_ref: Dict[str, float] = {
        'm2': 1.0,  # ! base unit
        'm\u00B2': 1.0,  # with unicode
        'cm2': 10000.0,
        'cm\u00B2': 10000.0,  # with unicode
        'mm2': 1.0e6,
        'mm\u00B2': 1.0e6,  # with unicode
        'km2': 1.0e-6,
        'km\u00B2': 1.0e-6,  # with unicode
        'dm2': 100.0,
        'dm\u00B2': 100.0,  # with unicode
        'ft2': 10.7639,
        'ft\u00B2': 10.7639,  # with unicode
        'in2': 1550.0031,
        'in\u00B2': 1550.0031,  # with unicode
        'yd2': 1.19599,
        'yd\u00B2': 1.19599,  # with unicode
        'ha': 1.0e-4,
        'hectare': 1.0e-4,
        'acre': 2.47105e-4
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
        'N.s/m²': 0.1,
        'μP': 1e6,
        'lb/ft.s': 0.671968,
        'lb/ft.h': 241.908
    }

    # SECTION: Flow-rate Conversions
    _flow_rate_conversions_ref: Dict[str, float] = {
        # molar basis
        "mol/s": 1.0,
        "mmol/s": 1000.0,
        "kmol/s": 0.001,
        "mol/min": 60.0,
        "kmol/min": 0.06,
        "mol/h": 3600.0,
        "mol/hr": 3600.0,
        "kmol/h": 3.6,
        "kmol/hr": 3.6,
        "kmol/day": 86400.0,
        # mass basis
        "kg/s": 1.0,
        "g/s": 1000.0,
        "kg/min": 60.0,
        "g/min": 60000.0,
        "kg/h": 3600.0,
        "kg/hr": 3600.0,
        "g/h": 3600000.0,
        "g/hr": 3600000.0,
        "tonne/s": 0.001,
        "lb/s": 453.592,
        "lbm/s": 453.592,
        "slug/s": 14.5939,
        "lbm/min": 27215.4,
        "slug/min": 875.632,
        "lbm/h": 1632924.0,
        "lbm/hr": 1632924.0,
        "slug/h": 52537.9,
        "slug/hr": 52537.9,
        "tonne/day": 86.4,
        "lbm/day": 39.4624e6,
        "slug/day": 1260912.0,
        "tonne/h": 3.6,
        "tonne/hr": 3.6,
        # volume basis
        "m3/s": 1.0,
        "m³/s": 1.0,          # if you want Unicode
        "L/s": 1000.0,
        "l/s": 1000.0,
        "cm3/s": 1e6,
        "cm³/s": 1e6,        # if you want Unicode
        "mL/s": 1e6,
        "m3/min": 60.0,
        "m³/min": 60.0,      # if you want Unicode
        "L/min": 60000.0,
        "l/min": 60000.0,
        "mL/min": 6e7,
        "m3/h": 3600.0,
        "m³/h": 3600.0,      # if you want Unicode
        "m3/hr": 3600.0,
        "m³/hr": 3600.0,      # if you want Unicode
        "L/h": 3600000.0,
        "L/hr": 3600000.0,
        "l/h": 3600000.0,
        "l/hr": 3600000.0,
        "mL/h": 3.6e9,
        "ft3/s": 35.3147,
        "ft³/s": 35.3147,      # if you want Unicode
        "ft3/min": 2118.88,
        "ft³/min": 2118.88,    # if you want Unicode
        "ft3/h": 127132.8,
        "ft³/h": 127132.8,     # if you want Unicode
        "ft3/hr": 127132.8,
        "ft³/hr": 127132.8,     # if you want Unicode
        "gal/s": 264.172,
        "gal/min": 15850.3,
        "bbl/day": 1.84013e-6,   # slightly more precise
        "barrel/day": 1.84013e-6,
    }

    # SECTION: Reference
    _reference = {
        'PRESSURE': _pressure_conversions_ref,
        'TEMPERATURE': _temperature_conversions_ref,
        'DENSITY': _density_conversions_ref,
        'CONCENTRATION': _concentration_conversions_ref,
        'ENERGY': _energy_conversions_ref,
        'GIBBS_FREE_ENERGY': _gibbs_free_energy_conversions_ref,
        'ENTHALPY': _enthalpy_conversions_ref,
        'HEAT_CAPACITY': _heat_capacity_conversions_ref,
        'HEAT_TRANSFER_COEFFICIENT': _heat_transfer_coefficient_ref,
        'VOLUME': _volume_conversions_ref,
        'MASS': _mass_conversions_ref,
        'MOLECULAR_WEIGHT': _molecular_weight_conversions_ref,
        'POWER': _power_conversions_ref,
        'LENGTH': _length_conversions_ref,
        'AREA': _area_conversions_ref,
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
    def concentration_conversions_ref(self):
        return self._concentration_conversions_ref

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
    def heat_transfer_coefficient_ref(self):
        return self._heat_transfer_coefficient_ref

    @property
    def volume_conversions_ref(self):
        return self._volume_conversions_ref

    @property
    def mass_conversions_ref(self):
        return self._mass_conversions_ref

    @property
    def molecular_weight_conversions_ref(self):
        return self._molecular_weight_conversions_ref

    @property
    def power_conversions_ref(self):
        return self._power_conversions_ref

    @property
    def length_conversions_ref(self):
        return self._length_conversions_ref

    @property
    def area_conversions_ref(self):
        return self._area_conversions_ref

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
