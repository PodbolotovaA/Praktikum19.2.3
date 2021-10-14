import pytest
from app.calculator import Calculator

import random
a = random.random()
b = random.random()
'''тесты будут проводиться на случайно сгенерированных числах'''

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, a, b) == a * b
        """тест на корректность выполнения метода умножения"""

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, a, b) == a / b
        """тест на корректность выполнения метода деления"""

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, a, b) == a - b
        """тест на корректность выполнения метода вычетания"""

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, a, b) == a + b
        """тест на корректность выполнения метода сложения"""