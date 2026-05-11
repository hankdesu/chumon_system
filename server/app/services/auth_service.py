from fastapi import Depends
from datetime import datetime, timezone

from app.core.auth import generate_session_data, verify_password
from app.dtos.staff_dto import LoginRequestDto, VerifySessionStaffDto
from app.repositories.staff_repository import StaffRepository
from app.repositories.staff_session_repository import StaffSessionRepository
from app.models.staff_session import StaffSession
from app.core.exceptions import (
    InvalidCredentialsException,
    InvalidSessionException,
    InvalidStaffException,
)
from app.core.db import AsyncDbSession


class AuthService:
    def __init__(
        self,
        db: AsyncDbSession,
        staff_repo: StaffRepository = Depends(),
        staff_session_repo: StaffSessionRepository = Depends(),
    ):
        self.db = db
        self.staff_repo = staff_repo
        self.staff_session_repo = staff_session_repo

    async def authenticate_staff(self, username: str, password: str):
        staff = await self.staff_repo.get_by_username(username)

        if not staff or not verify_password(password, staff.password):
            return None

        return staff

    async def login(self, login_data: LoginRequestDto):
        staff = await self.authenticate_staff(login_data.username, login_data.password)

        if not staff:
            raise InvalidCredentialsException

        if staff.id is None:
            raise Exception

        session_data = generate_session_data()

        db_staff_session = StaffSession(
            session_id=session_data["new_session_id"],
            staff_id=staff.id,
            expires_at=session_data["expire_date"],
        )
        await self.staff_session_repo.delete_expired_by_staff_id(
            staff.id, datetime.now(timezone.utc)
        )
        await self.staff_session_repo.create_staff_session(db_staff_session)
        await self.db.commit()

        return staff, session_data["new_session_id"]

    async def verify_session(self, session_id: str):
        session = await self.staff_session_repo.get_by_session_id(session_id)

        if (
            not session
            or session.expires_at is None
            or session.expires_at < datetime.now(timezone.utc)
        ):
            raise InvalidSessionException

        staff = await self.staff_repo.get_by_id(session.staff_id)

        if not staff:
            raise InvalidStaffException

        staff_dto = VerifySessionStaffDto(**staff.model_dump())

        return staff_dto
