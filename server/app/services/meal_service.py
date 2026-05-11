from fastapi import Depends

from app.core.db import AsyncDbSession
from app.dtos.query_params import FilterParams, OrderParams, PaginationParams
from app.models.meal import CreateMealDto, Meal, PatchMealDto
from app.repositories.meal_repository import MealRepository
from app.core.exceptions import DatabaseRecordNotFoundException


class MealService:
    def __init__(self, db: AsyncDbSession, meal_repo: MealRepository = Depends()):
        self.db = db
        self.meal_repo = meal_repo

    async def get_meals(
        self,
        page_params: PaginationParams,
        order_params: OrderParams,
        filter_params: FilterParams,
    ):
        meals = await self.meal_repo.get_meals(page_params, order_params, filter_params)

        return meals

    async def get_meal_by_id(self, meal_id: int):
        meal = await self.meal_repo.get_meal_by_id(meal_id)

        if meal is None:
            raise DatabaseRecordNotFoundException

        return meal

    async def create_meal(self, create_data: CreateMealDto):
        db_meal = Meal.model_validate(create_data)
        new_meal = await self.meal_repo.create_meal(db_meal)

        await self.db.commit()

        return new_meal

    async def patch_meal(self, meal_id: int, patch_data: PatchMealDto):
        db_meal = await self.meal_repo.get_meal_by_id(meal_id)

        if db_meal is None:
            raise DatabaseRecordNotFoundException

        for key, value in patch_data.model_dump(exclude_unset=True).items():
            setattr(db_meal, key, value)

        patched_meal = await self.meal_repo.patch_meal(db_meal)
        await self.db.commit()

        return patched_meal
