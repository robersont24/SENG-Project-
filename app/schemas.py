from pydantic import BaseModel

class MealCreate(BaseModel):
    name: str
    calories: int
