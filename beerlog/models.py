from re import S
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator
from statistics import mean
from datetime import datetime

class Beer(SQLModel, table=true):
    id: Optional(int) = Field(primary_key=True, default=True, index=True)
    name: str
    style: str
    flavor: str
    image: str
    cost: 10
    date: datetime = Field(default_factory = datetime.now())

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v
    
    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean(
            [
                values["flavor"],
                values["image"],
                values["cost"]
            ])
        return int(rate)

try:
    brewdog = Beer(name = "brewdog", style="IPA", flavor = 6, image = 8, cost = 10)
except RuntimeError:
    print("An error ocurred")