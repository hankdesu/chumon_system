from sqlmodel import SQLModel, Field, Column, Enum, DateTime, func, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

from app.enums.meal import MealStatus

if TYPE_CHECKING:
    from app.models.collection import Collection
    from app.models.type import Type


class MealBase(SQLModel):
    name: str | None = Field(default=None, nullable=True)
    description: str | None = Field(default=None, nullable=True)
    price: int = Field(nullable=False, default=0)
    status: MealStatus = Field(
        default=MealStatus.AVAILABLE,
        sa_column=Column(
            "status",
            Enum(MealStatus, name="meals_status_enum"),
            nullable=False,
        ),
    )
    type_id: int | None = Field(foreign_key="types.id", default=None, nullable=True)
    collection_id: int | None = Field(
        foreign_key="collections.id", default=None, nullable=True
    )


class CreateMealDto(MealBase):
    pass


class PatchMealDto(MealBase):
    pass


class Meal(MealBase, table=True):
    __tablename__ = "meals"  # type: ignore

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
    collection: "Collection" = Relationship(back_populates="meals")
    type: "Type" = Relationship(back_populates="meals")
