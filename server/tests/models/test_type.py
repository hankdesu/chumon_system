import pytest
from app.models.type import Type, TypeBase

def test_type_base_defaults():
    type_obj = TypeBase()
    assert type_obj.name is None
    assert type_obj.description is None

def test_type_base_values():
    type_obj = TypeBase(name="Main Dish", description="Primary courses")
    assert type_obj.name == "Main Dish"
    assert type_obj.description == "Primary courses"

def test_type_table_defaults():
    type_obj = Type()
    assert type_obj.id is None
    assert type_obj.name is None
    assert type_obj.description is None
    assert type_obj.created_at is None
    assert type_obj.updated_at is None

def test_type_table_values():
    type_obj = Type(id=1, name="Drink", description="Beverages")
    assert type_obj.id == 1
    assert type_obj.name == "Drink"
    assert type_obj.description == "Beverages"
