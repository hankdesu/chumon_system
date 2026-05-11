from fastapi import APIRouter, Depends

from app.models.staff import CreateStaffDto
from app.services.staff_service import StaffService
from app.dtos.response_dto import ResponseDto
from app.dtos.staff_dto import CreateStaffResponseDto
from app.core.deps import require_current_staff

router = APIRouter(
    tags=["Admin - Staffs"], dependencies=[Depends(require_current_staff)]
)


@router.post("/")
async def create_staff(
    create_data: CreateStaffDto,
    staff_service: StaffService = Depends(),
) -> ResponseDto[CreateStaffResponseDto]:
    new_staff = await staff_service.create_staff(create_data)
    new_staff_dto = CreateStaffResponseDto.model_validate(new_staff)

    return ResponseDto(data=new_staff_dto)
