from car import Car

# Base Decorator
class CarDecorator(Car):
    def __init__(self, car: Car):
        super().__init__(car.name, car.engine_type)
        self._car = car

    # Forward all behaviors to wrapped car
    def turn_on_engine(self):
        return self._car.turn_on_engine()

    def turn_off_engine(self):
        return self._car.turn_off_engine()

    def play_music(self):
        return self._car.play_music()

    def accelerate(self):
        return self._car.accelerate()

    def brake(self):
        return self._car.brake()

    def shift_gear(self, gear):
        return self._car.shift_gear(gear)


# --- Concrete Decorators ---
class SportsPackage(CarDecorator):
    def accelerate(self):
        if self._car.engine_on:
            self._car.speed += 20  # Faster acceleration
            print(f"{self._car.name} (Sports Package) zooms to {self._car.speed} km/h")
        else:
            print(f"Cannot accelerate, {self._car.name}'s engine is OFF")


class PremiumAudio(CarDecorator):
    def play_music(self):
        print(f"{self._car.name} (Premium Audio) is playing immersive surround sound")


class SafetyUpgrade(CarDecorator):
    def brake(self):
        if self._car.speed > 0:
            self._car.speed -= 15
            if self._car.speed < 0: 
                self._car.speed = 0
            print(f"{self._car.name} (Safety Upgrade) brakes smoothly to {self._car.speed} km/h")
        else:
            print(f"{self._car.name} is already stopped")
