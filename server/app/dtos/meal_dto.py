from pydantic import BaseModel, ConfigDict

from app.enums.meal import MealStatus


class MealBase(BaseModel):
    id: int
    name: str | None = None
    price: int = 0
    status: MealStatus = MealStatus.AVAILABLE
    collection_id: int | None = None

    model_config = ConfigDict(from_attributes=True)


class GetMealsResponseDto(BaseModel):
    meals: list[MealBase]


class GetMealResponseDto(MealBase):
    description: str | None = None
    type_id: int | None = None


class CreateMealResponseDto(MealBase):
    pass


class PatchMealResponseDto(MealBase):
    pass
