from tkinter import image_names
from typing import Optional, List
from sqlmodel import select
from database import get_session
from models import Beer

def add_beer_to_database(
    name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int,
 ) -> bool:
    
    with get_session() as session:
        beer = Beer(
            name = name,
            style = style,
            flavor = flavor,
            image = image,
            cost = cost            
        )
        session.add(beer) # INSERT INTO beer ...
        session.commit()
    return True