class Car:
    def __init__(self, name, engine_type):
        self.name = name
        self.engine_type = engine_type
        self.engine_on = False
        self.speed = 0
        self.gear = 0

    def turn_on_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"{self.name} engine ({self.engine_type}) is now ON")
        else:
            print(f"{self.name} engine is already ON")

    def turn_off_engine(self):
        if self.engine_on:
            self.engine_on = False
            print(f"{self.name} engine is now OFF")
        else:
            print(f"{self.name} engine is already OFF")

    def play_music(self):
        print(f"{self.name} is playing music 🎵")

    def accelerate(self):
        if self.engine_on:
            self.speed += 10
            print(f"{self.name} accelerates to {self.speed} km/h")
        else:
            print(f"Cannot accelerate, {self.name}'s engine is OFF")

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            print(f"{self.name} slows down to {self.speed} km/h")
        else:
            print(f"{self.name} is already stopped")

    def shift_gear(self, gear):
        self.gear = gear
        print(f"{self.name} shifts to gear {self.gear}")
