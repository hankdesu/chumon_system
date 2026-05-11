from typing import TYPE_CHECKING

from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, func

if TYPE_CHECKING:
    from app.models.meal import Meal
from datetime import datetime


class CollectionBase(SQLModel):
    name: str | None = Field(default=None, nullable=True)
    description: str | None = Field(default=None, nullable=True)


class Collection(CollectionBase, table=True):
    __tablename__ = "collections"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)

    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        ),
    )
    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        ),
    )
    meals: list["Meal"] = Relationship(back_populates="collection")
