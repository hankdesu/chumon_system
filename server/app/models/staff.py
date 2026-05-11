from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Column, Relationship, SQLModel, Field, DateTime, func, Enum

from app.enums.staff import StaffRole, ActiveStatus

if TYPE_CHECKING:
    from app.models.staff_session import StaffSession


class StaffBase(SQLModel):
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)
    role: StaffRole = Field(
        default=StaffRole.STAFF,
        sa_column=Column("role", Enum(StaffRole, name="staffs_role_enum")),
    )
    is_active: ActiveStatus = Field(
        default=ActiveStatus.ACTIVE,
        sa_column=Column("is_active", Enum(ActiveStatus, name="staffs_active_enum")),
    )


class CreateStaffDto(StaffBase):
    pass


class Staff(StaffBase, table=True):
    __tablename__ = "staffs"  # type: ignore

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
    staff_sessions: list["StaffSession"] = Relationship(back_populates="staff")
