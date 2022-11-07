"""
This moudule contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example
"""

# --------------------------------------
# import
# --------------------------------------

import pytest

# --------------------------------------
# A most basic test function
# --------------------------------------


@pytest.mark.math
def test_one_plus_one():
    assert 1+1 == 2


# --------------------------------------
# A most basic test function to show assertion introspection
# --------------------------------------
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

# --------------------------------------
# A most basic test function that verifies an exception
# --------------------------------------


@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0

    assert 'division by zero' in str(e.value)

# Multipication test ideas

# two positive integer
# identity:multiplying any number by 1
# zero: multiplying any number by 0
# postive by a negative
# negative by a negative
# multiply floats


# def test_multiply_two_positive_ints():
#     assert 2*3 == 6


# def test_multiply_identity():
#     assert 1*99 == 99


# def test_multiply_zero():
#     assert 0*100 == 0

# Violate DRY principle: Don't Repeat yourself

# -----------------------------------------------------------
# A parametrised test function
# -----------------------------------------------------------

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]


@pytest.mark.math
@pytest.mark.parametrize('a,b,product', products)
def test_multiplication(a, b, product):
    assert a*b == product

# look into the hypothesis library for specify parameter value instead of hardcode it by yourself
