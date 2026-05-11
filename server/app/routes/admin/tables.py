from fastapi import APIRouter, Depends

from app.core.deps import require_current_staff

router = APIRouter(
    tags=["Admin - Tables"], dependencies=[Depends(require_current_staff)]
)


@router.patch("/{table_id}")
async def patch_table(table_id: int):
    pass
