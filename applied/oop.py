"""
Examples of some object oriented programming idioms
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List

# Enum to represent vehicle types
class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    MOTORCYCLE = "Motorcycle"

# Abstract base class
class Vehicle(ABC):
    def __init__(self, model: str, year: int, vehicle_type: VehicleType):
        self._model = model
        self._year = year
        self._vehicle_type = vehicle_type

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @property
    def vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    @abstractmethod
    def start_engine(self) -> str:
        pass

# Dataclass to represent an Owner
@dataclass
class Owner:
    name: str
    age: int
    vehicles: List[Vehicle]

# Concrete class that extends the abstract Vehicle class
class Car(Vehicle):
    def __init__(self, model: str, year: int, mileage: int):
        super().__init__(model, year, VehicleType.CAR)
        self._mileage = mileage

    @property
    def mileage(self) -> int:
        return self._mileage

    @mileage.setter
    def mileage(self, value: int) -> None:
        if value < 0:
            raise ValueError("Mileage cannot be negative")
        self._mileage = value

    def start_engine(self) -> str:
        return f"The {self.model} engine is now running."

# Example usage
if __name__ == "__main__":
    car = Car("Tesla Model S", 2022, 15000)
    owner = Owner(name="Alice", age=35, vehicles=[car])

    print(f"Owner: {owner.name}, Age: {owner.age}")
    print(f"Vehicle: {car.model}, Year: {car.year}, Mileage: {car.mileage} miles")
    print(car.start_engine())

    # Update mileage using the property setter
    car.mileage = 16000
    print(f"Updated Mileage: {car.mileage} miles")