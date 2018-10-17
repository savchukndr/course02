import pytest
from mod01_db import Db


# session - wszedzie dostaną ten objekt
# packege - wszystkie testy w danym katologu dostana ten objekt
# module - wszystkie testy w tym module dostaną ten objekt
# class
# function (domyslne)
# Give realistic object Db


@pytest.fixture(scope='module')
def get_test_db():
    yield Db('test')
    print('dalej robie cos z baza')