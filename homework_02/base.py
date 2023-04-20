from abc import ABC
from .exceptions import LowFuelError, NotEnoughFuel
# import exceptions


class Vehicle(ABC):
    def __init__(self, weight: int = 1000, fuel: int = 100, fuel_consumption: int = 12):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: int):
        needed_fuel = distance * self.fuel_consumption
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel
        else:
            raise NotEnoughFuel
