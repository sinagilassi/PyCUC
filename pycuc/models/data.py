# import libs
import logging
from typing import TypedDict
import pycuc
# locals

# NOTE: setup logger
logger = logging.getLogger(__name__)

# define type


class InputData(TypedDict):
    value: int | float | str | None
    unit: str
    symbol: str


class ReferenceData(TypedDict):
    name: str
    symbol: str
    unit: str


class OutputData(TypedDict):
    value: float | None
    unit: str
    symbol: str
