import pytest

from mod01 import add, addRecord
from mod01_db import Db


def test_add():
    value = add(10, 10)
    assert value == 30


# Generartin paraments for test_add2 will be
# through decorator @pytest.mark.parametrize
@pytest.mark.parametrize('x,y,e', [
    (10,10,30),
    (20, 10, 40),
    (5, 5, 20)
])
def test_add2(x, y, e):
    assert add(x, y) == e


def test_add3():
    with pytest.raises(TypeError):
        add('d', 10)


@pytest.mark.xfail(raises=TypeError)
def test_add4():
    add('a', 2)


def test_addRecord(get_test_db):
    db = get_test_db
    addRecord(db, set())
    assert 1


def test_updateRecord(get_test_db):
    assert 1