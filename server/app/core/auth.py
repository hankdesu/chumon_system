from pwdlib import PasswordHash
import secrets
from datetime import datetime, timezone, timedelta
from typing import TypedDict

from app.core.config import settings


class SessionData(TypedDict):
    new_session_id: str
    expire_date: datetime


def verify_password(plain_password: str, hashed_password: str):
    password_hash = PasswordHash.recommended()

    return password_hash.verify(plain_password, hashed_password)


def generate_session_data() -> SessionData:
    new_session_id = secrets.token_urlsafe(settings.session_id_bytes)
    expire_date = datetime.now(timezone.utc) + timedelta(
        seconds=settings.session_expire_at
    )

    return {"new_session_id": new_session_id, "expire_date": expire_date}


def hash_password(password: str):
    password_hash = PasswordHash.recommended()

    return password_hash.hash(password)
