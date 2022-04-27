import warnings  # getting rid of SQL Alchemy warnings
from sqlalchemy.exc import SAWarning  # getting rid of SQL Alchemy warnings
from sqlmodel.sql.expression import (
    Select,
    SelectOfScalar,
)  # getting rid of SQL Alchemy warnings
from sqlmodel import create_engine, Session
from beerlog import models
from beerlog.config import settings

warnings.filterwarnings(
    "ignore", category=SAWarning
)  # getting rid of SQL Alchemy warnings
SelectOfScalar.inherit_cache = True  # getting rid of SQL Alchemy warnings
Select.inherit_cache = True  # getting rid of SQL Alchemy warnings


engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
