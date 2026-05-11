from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.deps import require_current_staff
from app.dtos.meal_dto import (
    CreateMealResponseDto,
    GetMealResponseDto,
    GetMealsResponseDto,
    MealBase,
    PatchMealResponseDto,
)
from app.dtos.query_params import FilterParams, OrderParams, PaginationParams
from app.dtos.response_dto import ResponseDto
from app.models.meal import CreateMealDto, PatchMealDto
from app.services.meal_service import MealService

router = APIRouter(
    tags=["Admin - Meals"], dependencies=[Depends(require_current_staff)]
)


@router.get("/")
async def get_meals(
    pagination_params: Annotated[PaginationParams, Depends()],
    order_params: Annotated[OrderParams, Depends()],
    filter_params: Annotated[FilterParams, Depends()],
    meal_service: MealService = Depends(),
) -> ResponseDto[GetMealsResponseDto]:
    db_meals = await meal_service.get_meals(
        pagination_params, order_params, filter_params
    )
    meals = [MealBase.model_validate(meal) for meal in db_meals]
    meals_dto = GetMealsResponseDto(meals=meals)

    return ResponseDto(data=meals_dto)


@router.get("/{meal_id}")
async def get_meal(
    meal_id: int, meal_service: MealService = Depends()
) -> ResponseDto[GetMealResponseDto]:
    db_meal = await meal_service.get_meal_by_id(meal_id)
    meal_dto = GetMealResponseDto.model_validate(db_meal)

    return ResponseDto(data=meal_dto)


@router.post("/")
async def create_meal(
    create_data: CreateMealDto, meal_service: MealService = Depends()
) -> ResponseDto[CreateMealResponseDto]:
    new_meal = await meal_service.create_meal(create_data)
    new_meal_dto = CreateMealResponseDto.model_validate(new_meal)

    return ResponseDto(data=new_meal_dto)


@router.patch("/{meal_id}")
async def patch_meal(
    meal_id: int, patch_data: PatchMealDto, meal_service: MealService = Depends()
) -> ResponseDto[PatchMealResponseDto]:
    patched_meal = await meal_service.patch_meal(meal_id, patch_data)
    patched_meal_dto = PatchMealResponseDto.model_validate(patched_meal)

    return ResponseDto(data=patched_meal_dto)
