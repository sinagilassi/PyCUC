# import libs
import logging
from typing import Dict, Optional, Any, TypedDict
import pycuc
# locals
from ..models import InputData, ReferenceData, OutputData
from ..docs.refs import Refs

# NOTE: setup logger
logger = logging.getLogger(__name__)


def map_to_reference(
    inputs: Dict[str, InputData],
    reference: Dict[str, ReferenceData],
    verbose: bool = False
) -> Optional[Dict[str, OutputData]]:
    """
    Map input values to reference units.

    Parameters
    ----------
    inputs : Dict[str, InputData]
        A dictionary containing input values with their units.
    reference : Dict[str, ReferenceData]
        A dictionary defining the reference units for each input.
    verbose : bool, optional
        Whether to print verbose output, by default False.

    Returns
    -------
    Dict[str, OutputData] | None
        A dictionary with input values converted to the reference units or None if an error occurs.
        The output dictionary contains keys including `value`, `symbol`, and `unit`.

    Notes
    -----
    This function uses the pycuc library to handle unit conversions.

    - `input_values` contains keys including value, symbol, and unit.
    - `input_reference` contains keys including name, symbol, and unit.
    - `output_values` contains keys including value, symbol, and unit.
    """
    try:
        # SECTION: Validate inputs
        if not isinstance(inputs, dict):
            raise ValueError("Inputs must be a dictionary")

        if not isinstance(reference, dict):
            raise ValueError("Reference must be a dictionary")

        if not isinstance(verbose, bool):
            raise ValueError("Verbose must be a boolean")

        # NOTE: >> check keys
        required_input_keys = set(InputData.__required_keys__)
        for key, value_dict in inputs.items():
            if not isinstance(value_dict, dict):
                raise ValueError(
                    f"Value for key '{key}' in inputs must be a dictionary."
                )
            if not required_input_keys.issubset(value_dict.keys()):
                missing_keys = required_input_keys - value_dict.keys()
                raise ValueError(
                    f"Input data for key '{key}' is missing required keys: {', '.join(missing_keys)}."
                )

        # NOTE: >> check keys
        required_reference_keys = set(ReferenceData.__required_keys__)
        for key, value_dict in reference.items():
            if not isinstance(value_dict, dict):
                raise ValueError(
                    f"Value for key '{key}' in reference must be a dictionary."
                )
            if not required_reference_keys.issubset(value_dict.keys()):
                missing_keys = required_reference_keys - value_dict.keys()
                raise ValueError(
                    f"Reference data for key '{key}' is missing required keys: {', '.join(missing_keys)}."
                )

        # SECTION: Map inputs to reference units
        # NOTE: Initialize the output dictionary
        output_values: Dict[str, OutputData] = {}

        # Iterate over each input value
        for key, value_dict in inputs.items():
            # Extract the value and its unit
            value = value_dict.get('value', None)
            unit = value_dict.get('unit', None)
            symbol = value_dict.get('symbol', None)

            # NOTE: Validate unit
            if unit is None:
                if verbose:
                    logger.warning(
                        f"Unit for key '{key}' is None. Skipping conversion."
                    )
                continue  # ! skip to next

            if Refs.is_unit_in_reference(unit) is False:
                if verbose:
                    logger.error(
                        f"Unit '{unit}' for key '{key}' not found in reference units. Skipping conversion."
                    )
                raise ValueError(
                    f"Unit '{unit}' for key '{key}' not found in reference units."
                )

            # NOTE: Get the reference unit for this input
            if key not in reference.keys():
                if verbose:
                    logger.warning(
                        f"Key '{key}' not found in reference dictionary. Skipping conversion."
                    )
                continue  # ! skip to next

            # set
            ref_unit = reference[key].get('unit', None)
            # >> check
            if ref_unit is None:
                if verbose:
                    logger.warning(
                        f"Reference unit for key '{key}' is None. Skipping conversion."
                    )
                continue  # ! skip to next

            # validate ref unit
            if Refs.is_unit_in_reference(ref_unit) is False:
                if verbose:
                    logger.error(
                        f"Reference unit '{ref_unit}' for key '{key}' not found in reference units. Skipping conversion."
                    )
                raise ValueError(
                    f"Reference unit '{ref_unit}' for key '{key}' not found in reference units."
                )

            # NOTE: check value
            if value is None:
                # verbose
                if verbose:
                    logger.warning(
                        f"Value for key '{key}' is None. Skipping conversion."
                    )
                # set None
                output_values[key] = OutputData(
                    value=None,
                    symbol=symbol,
                    unit=ref_unit
                )
                continue  # ! skip to next

            # NOTE: Type check for value
            try:
                value_float = float(value)
            except (TypeError, ValueError):
                if verbose:
                    logger.warning(
                        f"Value for key '{key}' ('{value}') is not convertible to float. Skipping conversion."
                    )
                # set None
                output_values[key] = OutputData(
                    value=None,
                    symbol=symbol,
                    unit=ref_unit
                )
                continue  # ! skip to next

            # NOTE: convert the value to the reference unit
            try:
                value_ref = pycuc.convert_from_to(value_float, unit, ref_unit)
            except Exception as conv_err:
                logger.error(f"Conversion error for key '{key}': {conv_err}")
                # set None
                output_values[key] = OutputData(
                    value=None,
                    symbol=symbol,
                    unit=ref_unit
                )
                continue  # ! skip to next

            output_values[key] = OutputData(
                value=value_ref,
                symbol=symbol,
                unit=ref_unit
            )

        # return output values
        return output_values
    except Exception as e:
        logger.error(f"Error in mapping unit inputs: {e}")
        return None
