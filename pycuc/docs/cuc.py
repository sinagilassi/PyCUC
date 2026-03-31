# CUSTOM UNIT CONVERTER
# ======================

# import packages/modules
import pandas as pd
from typing import Optional
# local
from .utils import Utils
from .refs import Refs


class CustomUnitConverter(Utils, Refs):
    # vars
    # NOTE: pressure
    _pressure_conversions = {}
    # NOTE: temperature
    _temperature_conversions = {}
    # NOTE: density
    _density_conversions = {}
    # NOTE: concentration
    _concentration_conversions = {}
    # NOTE: energy
    _energy_conversions = {}
    # NOTE: energy rate
    _energy_rate_conversions = {}
    # NOTE: gibbs free energy
    _gibbs_free_energy_conversions = {}
    # NOTE: enthalpy
    _enthalpy_conversions = {}
    # NOTE: heat capacity
    _heat_capacity_conversions = {}
    # NOTE: heat transfer coefficient
    _heat_transfer_coefficient_conversions = {}
    # NOTE: volume
    _volume_conversions = {}
    # NOTE: mass
    _mass_conversions = {}
    # NOTE: molecular weight
    _molecular_weight_conversions = {}
    # NOTE: power
    _power_conversions = {}
    # NOTE: length
    _length_conversions = {}
    # NOTE: area
    _area_conversions = {}
    # NOTE: force
    _force_conversions = {}
    # NOTE: viscosity
    _viscosity_conversions = {}
    # NOTE: flow rate
    _flow_rate_conversions = {}

    # Initialize empty custom conversions dictionary
    _custom_conversions = {}

    # load conversion unit
    _custom_conversions_full = {
        'CUSTOM': _custom_conversions
    }

    def __init__(self, value, unit, reference_file=''):
        self.value = value
        self.unit = str(unit).strip()
        self.reference_file = reference_file
        # utils init
        super().__init__()
        Refs().__init__()

        # NOTE: init vars
        self._pressure_conversions = self.pressure_conversions_ref
        self._temperature_conversions = self.temperature_conversions_ref
        self._density_conversions = self.density_conversions_ref
        self._concentration_conversions = self.concentration_conversions_ref
        self._energy_conversions = self.energy_conversions_ref
        self._energy_rate_conversions = self.energy_rate_conversions_ref
        self._gibbs_free_energy_conversions = self.gibbs_free_energy_conversions_ref
        self._enthalpy_conversions = self.enthalpy_conversions_ref
        self._heat_capacity_conversions = self.heat_capacity_conversions_ref
        self._heat_transfer_coefficient_conversions = self.heat_transfer_coefficient_ref
        self._volume_conversions = self.volume_conversions_ref
        self._mass_conversions = self.mass_conversions_ref
        self._molecular_weight_conversions = self.molecular_weight_conversions_ref
        self._power_conversions = self.power_conversions_ref
        self._length_conversions = self.length_conversions_ref
        self._area_conversions = self.area_conversions_ref
        self._force_conversions = self.force_conversions_ref
        self._viscosity_conversions = self.viscosity_conversions_ref
        self._flow_rate_conversions = self.flow_rate_conversions_ref

    def check_reference(
        self,
        reference: str,
        dataframe: bool = True
    ):
        '''
        Checks if the reference is valid

        Parameters
        ----------
        reference : str
            reference name such as pressure, temperature, custom, and ...
        dataframe : bool
            if True, return dataframe, else return dict

        Returns
        -------
        reference : dict | dataframe
            reference details
        '''
        try:
            # set
            reference = str(reference).strip().upper()

            # sub reference
            sub_reference = None

            # check
            if '::' in reference:
                # split
                reference_split = reference.split('::')
                # set
                reference = reference_split[1]
                sub_reference = reference

            # refs
            refs = {
                'PRESSURE': self._pressure_conversions,
                'TEMPERATURE': self._temperature_conversions,
                'CUSTOM': self._custom_conversions_full,
                'DENSITY': self._density_conversions,
                'CONCENTRATION': self._concentration_conversions,
                'ENERGY': self._energy_conversions,
                'ENERGY_RATE': self._energy_rate_conversions,
                'GIBBS_FREE_ENERGY': self._gibbs_free_energy_conversions,
                'ENTHALPY': self._enthalpy_conversions,
                'HEAT_CAPACITY': self._heat_capacity_conversions,
                'HEAT_TRANSFER_COEFFICIENT': self._heat_transfer_coefficient_conversions,
                'VOLUME': self._volume_conversions,
                'MASS': self._mass_conversions,
                'MOLECULAR_WEIGHT': self._molecular_weight_conversions,
                'POWER': self._power_conversions,
                'LENGTH': self._length_conversions,
                'AREA': self._area_conversions,
                'FORCE': self._force_conversions,
                'VISCOSITY': self._viscosity_conversions,
                'FLOW_RATE': self._flow_rate_conversions
            }

            # take all keys
            custom_keys = list(self._custom_conversions_full.keys())
            # all keys
            all_keys = list(set(list(refs.keys()) + custom_keys))

            # check
            if reference not in all_keys:
                raise Exception('Reference not found')

            # if contain ::
            if sub_reference:
                # set
                res = self._custom_conversions_full[sub_reference]
            elif reference == 'CUSTOM':
                res = self._custom_conversions_full['CUSTOM']
            else:
                # dict
                res = refs[reference]

            if dataframe:
                # Convert dictionary to DataFrame
                df = pd.DataFrame(
                    list(res.items()),
                    columns=['Unit', 'Value']
                )
                return df
            else:
                return res
        except Exception as e:
            raise Exception('Checking references failed!, ', e)

    def find_reference(
            self,
            from_unit: str,
            to_unit: str
    ):
        '''
        Finds the conversion function

        Parameters
        ----------
        from_unit : str
            from unit, e.g. 'bar', 'psi', 'C', 'F', 'K', 'R'
        to_unit : str
            to unit, e.g. 'bar', 'psi', 'C', 'F', 'K', 'R'

        Returns
        -------
        reference : str
            reference name such as pressure, temperature, custom
        '''
        try:
            # SECTION: reference
            reference = None
            # NOTE: pressure
            if (
                from_unit in self._pressure_conversions and
                    to_unit in self._pressure_conversions
            ):
                reference = 'PRESSURE'
            # NOTE: temperature
            elif (
                from_unit in self._temperature_conversions and
                to_unit in self._temperature_conversions
            ):
                reference = 'TEMPERATURE'
            # NOTE: density
            elif (
                from_unit in self._density_conversions and
                to_unit in self._density_conversions
            ):
                reference = 'DENSITY'
            # NOTE: concentration
            elif (
                from_unit in self._concentration_conversions and
                to_unit in self._concentration_conversions
            ):
                reference = 'CONCENTRATION'
            # NOTE: energy
            elif (
                from_unit in self._energy_conversions and
                to_unit in self._energy_conversions
            ):
                reference = 'ENERGY'
            # NOTE: energy rate
            elif (
                from_unit in self._energy_rate_conversions and
                to_unit in self._energy_rate_conversions
            ):
                reference = 'ENERGY_RATE'
            # NOTE: gibbs free energy
            elif (
                from_unit in self._gibbs_free_energy_conversions and
                to_unit in self._gibbs_free_energy_conversions
            ):
                reference = 'GIBBS_FREE_ENERGY'
            # NOTE: enthalpy
            elif (
                from_unit in self._enthalpy_conversions and
                    to_unit in self._enthalpy_conversions
            ):
                reference = 'ENTHALPY'
            # NOTE: heat capacity
            elif (
                from_unit in self._heat_capacity_conversions and
                to_unit in self._heat_capacity_conversions
            ):
                reference = 'HEAT_CAPACITY'
            # NOTE: heat transfer coefficient
            elif (
                from_unit in self._heat_transfer_coefficient_conversions and
                to_unit in self._heat_transfer_coefficient_conversions
            ):
                reference = 'HEAT_TRANSFER_COEFFICIENT'
            # NOTE: volume
            elif (
                from_unit in self._volume_conversions and
                to_unit in self._volume_conversions
            ):
                reference = 'VOLUME'
            # NOTE: mass
            elif (
                from_unit in self._mass_conversions and
                to_unit in self._mass_conversions
            ):
                reference = 'MASS'
            # NOTE: molecular weight
            elif (
                from_unit in self._molecular_weight_conversions and
                to_unit in self._molecular_weight_conversions
            ):
                reference = 'MOLECULAR_WEIGHT'
            # NOTE: power
            elif (
                from_unit in self._power_conversions and
                to_unit in self._power_conversions
            ):
                reference = 'POWER'
            # NOTE: length
            elif (
                from_unit in self._length_conversions and
                to_unit in self._length_conversions
            ):
                reference = 'LENGTH'
            # NOTE: area
            elif (
                from_unit in self._area_conversions and
                to_unit in self._area_conversions
            ):
                reference = 'AREA'
            # NOTE: force
            elif (
                from_unit in self._force_conversions and
                to_unit in self._force_conversions
            ):
                reference = 'FORCE'
            # NOTE: viscosity
            elif (
                from_unit in self._viscosity_conversions and
                to_unit in self._viscosity_conversions
            ):
                reference = 'VISCOSITY'
            # NOTE: flow rate
            elif (
                from_unit in self._flow_rate_conversions and
                to_unit in self._flow_rate_conversions
            ):
                reference = 'FLOW_RATE'
            # SECTION: custom
            elif (
                from_unit in self._custom_conversions and
                to_unit in self._custom_conversions
            ):
                reference = 'CUSTOM'
            else:
                # check
                for key, value in self._custom_conversions_full.items():
                    if from_unit in value and to_unit in value:
                        reference = 'CUSTOM'

            # check
            if reference is None:
                raise Exception('Conversion units not found')

            return reference
        except Exception as e:
            raise Exception('Finding reference failed!, ', e)

    def check_conversion_block(self, conversion_block: str):
        '''
        Checks conversion block, such as 'bar => psi', 'C => F', 'F => C', 'K => C', 'R => C'

        Parameters
        ----------
        conversion_block : str
            conversion block

        Returns
        -------
        subgroups : list
            list of subgroups. [0] = from_unit, [1] = '=>', [2] = to_unit
        '''
        try:
            return self.parse_conversion_block(conversion_block)
        except Exception as e:
            raise Exception("Checking conversion block failed!, ", e)

    def convert(
        self,
        to_unit: str,
        reference: Optional[str] = None
    ):
        '''
        Selects the conversion function

        Parameters
        ----------
        to_unit : str
            to unit, e.g. 'bar', 'psi', 'C', 'F', 'K', 'R'
        reference : str
            reference name such as pressure, temperature, custom

        Returns
        -------
        res : float
            converted value
        '''
        try:
            # find reference
            if reference is None:
                reference = self.find_reference(self.unit, to_unit)

            # upper
            reference = reference.upper()

            # reference
            ref = {
                # SECTION: predefined
                'PRESSURE': self._pressure_conversions,
                'TEMPERATURE': self._temperature_conversions,
                'DENSITY': self._density_conversions,
                'CONCENTRATION': self._concentration_conversions,
                'ENERGY': self._energy_conversions,
                'ENERGY_RATE': self._energy_rate_conversions,
                'GIBBS_FREE_ENERGY': self._gibbs_free_energy_conversions,
                'ENTHALPY': self._enthalpy_conversions,
                'HEAT_CAPACITY': self._heat_capacity_conversions,
                'HEAT_TRANSFER_COEFFICIENT': self._heat_transfer_coefficient_conversions,
                'VOLUME': self._volume_conversions,
                'MASS': self._mass_conversions,
                'MOLECULAR_WEIGHT': self._molecular_weight_conversions,
                'POWER': self._power_conversions,
                'LENGTH': self._length_conversions,
                'AREA': self._area_conversions,
                'FORCE': self._force_conversions,
                'VISCOSITY': self._viscosity_conversions,
                'FLOW_RATE': self._flow_rate_conversions,
                # SECTION: custom
                'CUSTOM': self._custom_conversions
            }

            # check
            if reference not in ref.keys():
                raise Exception('Reference not found')

            # reference
            ref_methods = {
                # SECTION: predefined
                'PRESSURE': lambda x: self.convert_pressure(x),
                'TEMPERATURE': lambda x: self.convert_temperature(x),
                'DENSITY': lambda x: self.convert_X(x, 'DENSITY'),
                'CONCENTRATION': lambda x: self.convert_X(x, 'CONCENTRATION'),
                'ENERGY': lambda x: self.convert_X(x, 'ENERGY'),
                'ENERGY_RATE': lambda x: self.convert_X(x, 'ENERGY_RATE'),
                'GIBBS_FREE_ENERGY': lambda x: self.convert_X(x, 'GIBBS_FREE_ENERGY'),
                'ENTHALPY': lambda x: self.convert_X(x, 'ENTHALPY'),
                'HEAT_CAPACITY': lambda x: self.convert_X(x, 'HEAT_CAPACITY'),
                'HEAT_TRANSFER_COEFFICIENT': lambda x: self.convert_X(x, 'HEAT_TRANSFER_COEFFICIENT'),
                'VOLUME': lambda x: self.convert_X(x, 'VOLUME'),
                'MASS': lambda x: self.convert_X(x, 'MASS'),
                'MOLECULAR_WEIGHT': lambda x: self.convert_X(x, 'MOLECULAR_WEIGHT'),
                'POWER': lambda x: self.convert_X(x, 'POWER'),
                'LENGTH': lambda x: self.convert_X(x, 'LENGTH'),
                'AREA': lambda x: self.convert_X(x, 'AREA'),
                'FORCE': lambda x: self.convert_X(x, 'FORCE'),
                'VISCOSITY': lambda x: self.convert_X(x, 'VISCOSITY'),
                'FLOW_RATE': lambda x: self.convert_X(x, 'FLOW_RATE'),
                # SECTION: custom
                'CUSTOM': lambda x: self.convert_custom(x)
            }

            # check
            if reference not in ref_methods:
                raise Exception('Reference not found')

            # set
            res = ref_methods[reference](to_unit)

            return res
        except Exception as e:
            raise Exception('Setting conversion function failed!, ', e)

    def convert_X(
        self,
        to_unit: str,
        reference_name: str
    ):
        '''
        Converts a value from one unit to another, using the reference dictionary.

        Parameters
        ----------
        to_unit : str
            to unit
        reference_name : str
            reference name such as pressure, temperature, custom

        Returns
        -------
        float
            converted value
        '''
        try:
            # set
            from_unit = self.unit
            # res
            from_factor = float(self._reference[reference_name][from_unit])
            to_factor = float(self._reference[reference_name][to_unit])
            return float(self.value) / from_factor * to_factor

        except Exception as e:
            raise ValueError(
                f"{reference_name} conversion failed from '{self.unit}' to '{to_unit}': {e}"
            ) from e

    def convert_pressure(self, to_unit: str):
        '''
        Converts pressure from one unit to another.

        Parameters
        ----------
        to_unit : str
            to unit

        Returns
        -------
        float
            converted value
        '''
        try:
            # set
            from_unit = self.unit
            # res
            from_factor = float(self._pressure_conversions[from_unit])
            to_factor = float(self._pressure_conversions[to_unit])
            return float(self.value) / from_factor * to_factor

        except Exception as e:
            raise Exception('Pressure conversion failed!, ', e)

    def convert_temperature(self, to_unit: str):
        '''
        Converts temperature from one unit to another.

        Parameters
        ----------
        to_unit : str
            to unit

        Returns
        -------
        float
            converted value
        '''
        try:
            # set
            from_unit = self.unit
            value = float(self.value)

            # Convert to Celsius first
            if from_unit == 'F':
                value = (
                    value - self._temperature_conversions[from_unit]) * 5/9
            elif from_unit == 'K':
                value = value + self._temperature_conversions[from_unit]
            elif from_unit == 'R':
                value = (
                    value - self._temperature_conversions[from_unit]) * 5/9

            # Convert from Celsius to target unit
            if to_unit == 'F':
                result = value * 9/5 + self._temperature_conversions[to_unit]
            elif to_unit == 'K':
                result = value - self._temperature_conversions[to_unit]
            elif to_unit == 'R':
                result = value * 9/5 + self._temperature_conversions[to_unit]
            else:  # ! to_unit == 'C'
                result = value

            return result
        except Exception as e:
            raise Exception('Temperature conversion failed!, ', e)

    def add_custom_unit(self, unit: str, conversion_factor: float):
        '''
        Adds a custom unit conversion to the reference dictionary

        Parameters
        ----------
        unit : str
            unit
        conversion_factor : float
            conversion factor

        Returns
        -------
        bool
            True if successful
        '''
        try:
            # add
            self._custom_conversions[unit] = conversion_factor
            return True
        except Exception as e:
            raise Exception('Adding new unit failed!, ', e)

    def load_custom_unit(self, f: str):
        '''
        Load custom unit

        Parameters
        ----------
        f : str
            yml file path

        Returns
        -------
        dict
            custom unit
        '''
        try:
            # custom unit
            custom_unit = self._load_custom_conversion_unit(f)

            # if not empty
            if len(custom_unit) == 0:
                return False

            # check key 'CUSTOM-UNIT'
            if 'CUSTOM-UNIT' not in custom_unit.keys():
                raise ValueError("Key 'CUSTOM-UNIT' not found")

            # update custom conversion
            for key, value in custom_unit['CUSTOM-UNIT'].items():
                self._custom_conversions_full[str(key).strip()] = value

            return self._custom_conversions_full

        except Exception as e:
            raise Exception('Loading custom unit failed!, ', e)

    def convert_custom(self, to_unit: str):
        '''
        Converts using custom units

        Parameters
        ----------
        to_unit : str
            to unit

        Returns
        -------
        float
            converted value
        '''
        try:
            # set
            from_unit = self.unit

            # looping through all keys in _custom_conversions_full
            for key, custom_unit_dict in self._custom_conversions_full.items():

                # check
                if (from_unit in custom_unit_dict and
                        to_unit in custom_unit_dict):
                    # set
                    from_val = float(custom_unit_dict[from_unit])
                    to_val = float(custom_unit_dict[to_unit])
                    return float(self.value) / from_val * to_val

            raise ValueError("Custom conversion units not found")
        except Exception as e:
            raise Exception('Conversion failed!, ', e)
