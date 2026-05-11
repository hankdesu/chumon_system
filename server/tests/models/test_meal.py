import pytest
from pydantic import ValidationError
from app.models.meal import Meal, MealBase, CreateMealDto, PatchMealDto
from app.enums.meal import MealStatus

def test_meal_base_defaults():
    meal = MealBase()
    assert meal.name is None
    assert meal.description is None
    assert meal.price == 0
    assert meal.status == MealStatus.AVAILABLE
    assert meal.type_id is None
    assert meal.collection_id is None

def test_meal_base_values():
    meal = MealBase(
        name="Burger",
        description="Juicy beef burger",
        price=150,
        status=MealStatus.SOLD_OUT,
        type_id=1,
        collection_id=2
    )
    assert meal.name == "Burger"
    assert meal.description == "Juicy beef burger"
    assert meal.price == 150
    assert meal.status == MealStatus.SOLD_OUT
    assert meal.type_id == 1
    assert meal.collection_id == 2

def test_meal_table_defaults():
    meal = Meal()
    assert meal.id is None
    assert meal.price == 0
    assert meal.status == MealStatus.AVAILABLE

def test_create_meal_dto():
    dto = CreateMealDto(name="Pizza", price=200)
    assert dto.name == "Pizza"
    assert dto.price == 200

def test_patch_meal_dto():
    dto = PatchMealDto(price=180)
    assert dto.price == 180
    assert dto.name is None

def test_meal_invalid_price_type():
    with pytest.raises(ValidationError):
        # price should be int
        MealBase(price="not-an-int")
