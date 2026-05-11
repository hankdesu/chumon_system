from fastapi import Cookie, Depends

from app.core.exceptions import AuthenticationRequiredException
from app.services.auth_service import AuthService


async def require_current_staff(
    chumon_session_id: str | None = Cookie(default=None),
    auth_service: AuthService = Depends(),
):
    if not chumon_session_id:
        raise AuthenticationRequiredException
    return await auth_service.verify_session(chumon_session_id)
