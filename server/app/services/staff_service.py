from fastapi import Depends

from app.repositories.staff_repository import StaffRepository
from app.models.staff import CreateStaffDto
from app.core.db import AsyncDbSession
from app.core.auth import hash_password
from app.models.staff import Staff


class StaffService:
    def __init__(self, db: AsyncDbSession, staff_repo: StaffRepository = Depends()):
        self.db = db
        self.staff_repo = staff_repo

    async def create_staff(self, create_data: CreateStaffDto):
        hashed_password = hash_password(create_data.password)

        db_staff = Staff.model_validate(create_data)
        db_staff.password = hashed_password
        new_staff = await self.staff_repo.create_staff(db_staff)

        await self.db.commit()

        return new_staff
