from factory import CarFactory
from management import CarManager
from rules import SportsCarRule, SUVRule, SedanRule
from decorators import SportsPackage, PremiumAudio, SafetyUpgrade

if __name__ == "__main__":
    factory = CarFactory()
    manager = CarManager()

    # Setup rules chain
    rules = SportsCarRule(SUVRule(SedanRule()))

    # Example car orders
    orders = [
        ("Sedan", "Hybrid"),
        ("SUV", "Diesel"),
        ("SportsCar", "Gasoline"),
    ]

    for car_type, engine_type in orders:
        print(f"\nOrdering: {car_type} with {engine_type} engine")
        if rules.handle(car_type, engine_type):
            car = factory.create_car(car_type, engine_type)

            # Apply customizations depending on type
            if car_type == "SportsCar":
                car = SportsPackage(car)   # Sports boost
                car = PremiumAudio(car)    # Extra audio
            elif car_type == "SUV":
                car = SafetyUpgrade(car)   # Better braking
            elif car_type == "Sedan":
                car = PremiumAudio(car)    # Just luxury sound

            manager.add_car(car)

    print("\n--- Final Production List ---")
    manager.list_cars()

    print("\n--- Demonstrating Features ---")
    for car in manager.cars:
        car.turn_on_engine()
        car.accelerate()
        car.play_music()
        car.brake()
        car.shift_gear(2)
        car.turn_off_engine()
        print()
