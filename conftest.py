import pytest
from unittest.mock import patch
from sqlmodel import create_engine
from beerlog import models


@pytest.fixture(autouse=True, scope="function")
def each_test_uses_separate_database(request):
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = tmpdir.join("beerlog.test.db")
    engine = create_engine(f"sqlite:///{test_db}")
    models.SQLModel.metadata.create_all(bind=engine)
    with patch(
        "beerlog.database.engine", engine
    ):  # o patch faz com que toda vez que este objeto for utilizado, ele seja alterado para o engine desejado aqui
        yield  # Funciona como um return so que gera conteudo. Ele eh um return mais poderoso
