from sqlmodel import SQLModel, Field, Column, DateTime, func, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.meal import Meal


class TypeBase(SQLModel):
    name: str | None = Field(default=None, nullable=True)
    description: str | None = Field(default=None, nullable=True)


class Type(TypeBase, table=True):
    __tablename__ = "types"  # type: ignore

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
    meals: list["Meal"] = Relationship(back_populates="type")
