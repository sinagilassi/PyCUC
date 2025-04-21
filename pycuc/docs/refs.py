# REFERENCE CLASS
# ================

# import module/packages


# local

class Refs:

    # vars
    # SECTION: Pressure Conversions
    _pressure_conversions_ref = {
        'bar': 1.0,
        'mbar': 1000.0,
        'ubar': 1000000.0,
        'Pa': 100000.0,
        'hPa': 1000.0,
        'kPa': 100.0,
        'MPa': 0.1,
        'kgcm2': 1.01972,
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
    _temperature_conversions_ref = {
        'C': 0,  # Celsius
        'F': 32,  # Fahrenheit
        'K': -273.15,  # Kelvin
        'R': 491.67  # Rankine
    }

    # SECTION: Density Conversions
    _density_conversions_ref = {
        'g/cm3': 1.0,
        'kg/dm3': 1.0,
        't/m3': 1.0,
        'kg/m3': 1000.0,
        'lb/ft3': 62.42796,
        'lb/in3': 0.0361273,
    }

    # SECTION: Energy Conversions
    _energy_conversions_ref = {
        'J': 1.0,
        'kJ': 0.001,
        'cal': 0.239006,
        'kcal': 0.000239006,
        'Wh': 0.000277778,
        'kWh': 2.77778e-7,
        'BTU': 0.000947817,
        'ft-lb': 0.737562
    }

    # SECTION: Heat capacity Conversions
    _heat_capacity_conversions_ref = {
        'J/kg.K': 1.0,
        'kJ/kg.K': 0.001,
        'cal/kg.K': 0.239006,
        'kcal/kg.K': 0.000239006,
        'cal/g.K': 0.000239006,
        'J/g.K': 0.001,
        'kJ/g.K': 1.0e-6,
        'BTU/lb.F': 0.000238846,
    }

    # SECTION: Volume Conversions
    _volume_conversions_ref = {
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
    _mass_conversions_ref = {
        'kg': 1.0,
        'g': 1000.0,
        'mg': 1000000.0,
        'lb': 2.20462,
        'oz': 35.274,
        't': 0.001,
        'st': 0.157473
    }

    # SECTION: Power Conversions
    _power_conversions_ref = {
        'W': 1.0,
        'kW': 0.001,
        'MW': 1e-6,
        'GW': 1e-9,
        'HP': 0.00134102,
        'BTU/h': 3.41214,
        'ft-lb/min': 0.737562
    }

    # SECTION: Length Conversions
    _length_conversions_ref = {
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
    _force_conversions_ref = {
        'N': 1.0,
        'kN': 0.001,
        'lbf': 0.224809,
        'kgf': 0.101972,
        'dyn': 100000,
        'ozf': 35.274
    }

    # SECTION: Reference
    _reference = {
        'PRESSURE': _pressure_conversions_ref,
        'TEMPERATURE': _temperature_conversions_ref,
        'DENSITY': _density_conversions_ref,
        'ENERGY': _energy_conversions_ref,
        'HEAT_CAPACITY': _heat_capacity_conversions_ref,
        'VOLUME': _volume_conversions_ref,
        'MASS': _mass_conversions_ref,
        'POWER': _power_conversions_ref,
        'LENGTH': _length_conversions_ref,
        'FORCE': _force_conversions_ref
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
