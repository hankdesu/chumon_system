from typing import Any

from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlmodel import col, or_, select

from app.core.db import AsyncDbSession
from app.dtos.query_params import FilterParams, OrderParams, PaginationParams
from app.models.meal import Meal


class MealRepository:
    def __init__(self, db_session: AsyncDbSession):
        self.db_session = db_session

    async def get_meals(
        self,
        page_params: PaginationParams,
        order_params: OrderParams,
        filter_params: FilterParams,
    ):
        query = select(Meal)

        if filter_params.query:
            query = query.where(
                or_(
                    col(Meal.name).contains(filter_params.query),
                    col(Meal.description).contains(filter_params.query),
                )
            )

        valid_columns = Meal.model_fields.keys()

        if order_params.sort_by in valid_columns:
            sort_column: InstrumentedAttribute[Any] = getattr(
                Meal, order_params.sort_by
            )

            if order_params.order == "desc":
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column)
        else:
            query = query.order_by(col(Meal.created_at).desc())

        query = query.offset(page_params.offset).limit(page_params.limit)

        result = await self.db_session.execute(query)

        return result.scalars().all()

    async def get_meal_by_id(self, meal_id: int):
        meal = await self.db_session.get(Meal, meal_id)

        return meal

    async def create_meal(self, meal_data: Meal):
        self.db_session.add(meal_data)

        await self.db_session.flush()

        return meal_data

    async def patch_meal(self, meal_data: Meal):
        self.db_session.add(meal_data)
        await self.db_session.flush()

        return meal_data
