from sqlmodel import select

from app.core.db import AsyncDbSession
from app.models.staff import Staff


class StaffRepository:
    def __init__(self, db_session: AsyncDbSession):
        self.db_session = db_session

    async def get_by_username(self, username: str):
        result = await self.db_session.execute(
            select(Staff).where(Staff.username == username)
        )

        return result.scalar_one_or_none()

    async def get_by_id(self, staff_id: int):
        return await self.db_session.get(Staff, staff_id)

    async def create_staff(self, db_staff: Staff):
        self.db_session.add(db_staff)

        await self.db_session.flush()

        return db_staff
