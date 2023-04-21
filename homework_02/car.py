from .base import Vehicle
from .engine import Engine
"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car (Vehicle):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine
