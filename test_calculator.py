import pytest

from calculator import Calculator

class TestCalculator():
    def test_sum(self):
        calculator = Calculator(1, 2)
        assert calculator.sum() == 3

    def test_sub(self):
        calculator = Calculator(1, 2)
        assert calculator.sub() == -1

    def test_mul(self):
        calculator = Calculator(1, 2)
        assert calculator.mul() == 2

    def test_div(self):
        calculator = Calculator(1, 2)
        assert calculator.div() == 0.5