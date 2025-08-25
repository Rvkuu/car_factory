from typing import List, Optional

class CarManager:
    _instance: Optional["CarManager"] = None   # class-level singleton reference

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # initialize only once
        if not hasattr(self, "cars"):
            self.cars: List = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"CarManager: {car.name} with {car.engine_type} engine added to production list")

    def list_cars(self):
        for car in self.cars:
            print(f"- {car.name} ({car.engine_type})")
