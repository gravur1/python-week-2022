from typing import List
from fastapi import FastAPI
from beerlog.core import get_beers_from_database
from beerlog.serializers import BeerOut, BeerIn
from beerlog.database import get_session
from beerlog.models import Beer

# to start web API run:
# python -m uvicorn beerlog.api:api --reload

api = FastAPI(title="Beerlog")

# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/docs


@api.get("/beers/", response_model=List[BeerOut])
async def list_beers():
    """Lists beers from the database"""
    beers = get_beers_from_database()
    return beers


@api.post("/beers/", response_model=BeerOut)
async def add_beer(beer_in: BeerIn):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    return beer
