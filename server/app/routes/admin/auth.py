from typing import Annotated

from fastapi import APIRouter, Body, Depends, Response

from app.core.config import settings
from app.dtos.response_dto import ResponseDto
from app.dtos.staff_dto import LoginRequestDto, LoginResponseDto
from app.services.auth_service import AuthService


router = APIRouter(tags=["Admin - Auth"])


@router.post("/login")
async def staff_login(
    login_data: Annotated[LoginRequestDto, Body],
    response: Response,
    auth_service: AuthService = Depends(),
) -> ResponseDto[LoginResponseDto]:
    staff, new_session_id = await auth_service.login(login_data)

    response.set_cookie(
        key="chumon_session_id",
        value=new_session_id,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=settings.session_expire_at,
    )

    return ResponseDto(data=LoginResponseDto.model_validate(staff))
