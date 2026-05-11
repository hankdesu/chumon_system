from pydantic import BaseModel, Field, ConfigDict

from app.core.validators import NoSpaceStr
from app.enums.staff import ActiveStatus


class LoginRequestDto(BaseModel):
    username: NoSpaceStr
    password: NoSpaceStr = Field(min_length=8, max_length=20)


class LoginResponseDto(BaseModel):
    id: int
    username: str
    role: str
    is_active: ActiveStatus

    model_config = ConfigDict(from_attributes=True)


class CreateStaffResponseDto(LoginResponseDto):
    pass


class VerifySessionStaffDto(LoginResponseDto):
    pass
