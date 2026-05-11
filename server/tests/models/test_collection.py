import pytest
from pydantic import ValidationError
from app.models.collection import Collection, CollectionBase

def test_collection_base_defaults():
    collection = CollectionBase()
    assert collection.name is None
    assert collection.description is None

def test_collection_base_values():
    collection = CollectionBase(name="Breakfast", description="Morning meals")
    assert collection.name == "Breakfast"
    assert collection.description == "Morning meals"

def test_collection_table_defaults():
    collection = Collection()
    assert collection.id is None
    assert collection.name is None
    assert collection.description is None
    # created_at and updated_at are handled by the database (server_default)
    # but in SQLModel/Pydantic they default to None if not provided
    assert collection.created_at is None
    assert collection.updated_at is None

def test_collection_table_values():
    collection = Collection(id=1, name="Lunch", description="Midday meals")
    assert collection.id == 1
    assert collection.name == "Lunch"
    assert collection.description == "Midday meals"
