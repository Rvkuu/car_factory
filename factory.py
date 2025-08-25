from car import Car

class CarFactory:
    def create_car(self, car_type, engine_type="Gasoline"):
        if car_type == "Sedan":
            return Car("Sedan", engine_type)
        elif car_type == "SUV":
            return Car("SUV", engine_type)
        elif car_type == "SportsCar":
            return Car("SportsCar", engine_type)
        else:
            raise ValueError(f"Unknown car type: {car_type}")
