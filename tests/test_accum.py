"""
This moudule contains basic unit tests for the accu module.
Their purpose is to show how to use the pytest framework by example.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

import pytest
from stuff.accum import Accumulator


# ------------------------------------------
# Fixtures
# -----------------------------------------

@pytest.fixture
def accum():
    return Accumulator()


"""
@pytest.fixture
def accum(scope="session"):
    return Accumulator()
    
pytest will only one the fixture once and stored the return value. If other 
function call the method again, pytest will inject the value as result of that call
It will be useful when we have to read the value from other file
"""

""" 
# become generator if keyword yield is used
Every statment before the yield statment is the setup steps 
and clean up steps after it
"""


@pytest.fixture
def accum2():
    yield Accumulator()
    print("clean up")

# ------------------------------------------
# Tests
# -----------------------------------------


@pytest.mark.accumulator
# pytest will automatically look for fixture when there is an argument
def test_accumulator_init(accum, accum2):
    assert accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum):

    accum.add()
    assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):

    accum.add(3)
    assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):

    accum.add()
    accum.add()
    assert accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10
