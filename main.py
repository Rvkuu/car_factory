from factory import CarFactory
from management import CarManager

if __name__ == "__main__":
    factory = CarFactory()
    manager = CarManager()

    # Create different cars
    sedan = factory.create_car("Sedan", "Hybrid")
    suv = factory.create_car("SUV", "Diesel")
    sports = factory.create_car("SportsCar", "Gasoline")

    # Add to manager (Singleton)
    manager.add_car(sedan)
    manager.add_car(suv)
    manager.add_car(sports)

    print("\n--- Production List ---")
    manager.list_cars()

    print("\n--- Car Functions ---")
    sedan.turn_on_engine()
    sedan.play_music()
    sedan.shift_gear(1)
    sedan.accelerate()
    sedan.brake()
    sedan.turn_off_engine()
