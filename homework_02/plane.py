from .base import Vehicle
from .exceptions import CargoOverload
"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):

    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, new_cargo: int):
        if (self.cargo + new_cargo) <= self.max_cargo:
            self.cargo += new_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
