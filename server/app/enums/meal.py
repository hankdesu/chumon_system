from enum import Enum


class MealStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    SOLD_OUT = "SOLD_OUT"
    DISCONTINUED = "DISCONTINUED"
