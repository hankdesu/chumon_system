from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, SQLModel, Column, func, DateTime, Relationship

if TYPE_CHECKING:
    from app.models.staff import Staff


class StaffSessionBase(SQLModel):
    staff_id: int = Field(foreign_key="staffs.id", nullable=False)
    session_id: str = Field(nullable=False, index=True, unique=True)
    expires_at: datetime | None = Field(
        default=None, sa_column=Column(DateTime(timezone=True), nullable=False)
    )


class StaffSession(StaffSessionBase, table=True):
    __tablename__ = "staff_sessions"  # type: ignore

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
    staff: Staff = Relationship(back_populates="staff_sessions")
