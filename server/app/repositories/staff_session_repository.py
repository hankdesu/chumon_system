from sqlmodel import select, delete, col
from datetime import datetime, timezone

from app.core.db import AsyncDbSession
from app.models.staff_session import StaffSession


class StaffSessionRepository:
    def __init__(self, db_session: AsyncDbSession):
        self.db_session = db_session

    async def create_staff_session(self, staff_session_data: StaffSession):
        self.db_session.add(staff_session_data)

        await self.db_session.flush()

        return staff_session_data

    async def get_by_session_id(self, session_id: str):
        result = await self.db_session.execute(
            select(StaffSession).where(StaffSession.session_id == session_id)
        )

        return result.scalar_one_or_none()

    async def delete_by_staff_id(self, staff_id: int):
        result = await self.db_session.execute(
            delete(StaffSession).where(col(StaffSession.staff_id) == staff_id)
        )

        return result

    async def delete_expired_by_staff_id(
        self, staff_id: int, current_time: datetime | None = None
    ):
        if current_time is None:
            current_time = datetime.now(timezone.utc)

        result = await self.db_session.execute(
            delete(StaffSession).where(
                col(StaffSession.staff_id) == staff_id,
                col(StaffSession.expires_at) < current_time,
            )
        )

        return result
