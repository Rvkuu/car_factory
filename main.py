from factory import CarFactory
from management import CarManager
from rules import SportsCarRule, SUVRule, SedanRule

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
        ("SportsCar", "Diesel"),   # should fail
        ("SUV", "Electric"),       # should fail
    ]

    for car_type, engine_type in orders:
        print(f"\nOrdering: {car_type} with {engine_type} engine")
        if rules.handle(car_type, engine_type):
            car = factory.create_car(car_type, engine_type)
            manager.add_car(car)

    print("\n--- Final Production List ---")
    manager.list_cars()
