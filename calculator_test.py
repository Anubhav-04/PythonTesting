import calculator
import pytest

def test_add():
    assert calculator.add(2,3) == 5
    assert calculator.add(-2,3) == 1
    assert calculator.add(-2,-5) == -7

def test_sub():
    assert calculator.sub(2,3) == -1
    assert calculator.sub(5,-2) == 7
    assert calculator.sub(-2,-5) == 3

def test_mul():
    assert calculator.mul(2,3) == 6
    assert calculator.mul(-2,3) == -6
    assert calculator.mul(-2,-5) == 10

def test_div():
    assert calculator.div(8,2) == 4
    assert calculator.div(20,-5) == -4
    with pytest.raises(ZeroDivisionError):
        calculator.div(20, 0)