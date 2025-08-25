class RuleHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, car_type, engine_type):
        if self.next_handler:
            return self.next_handler.handle(car_type, engine_type)
        return True


class SportsCarRule(RuleHandler):
    def handle(self, car_type, engine_type):
        if car_type == "SportsCar" and engine_type in ["Diesel", "Electric"]:
            print(f"Rule Violation: SportsCar cannot have {engine_type} engine.")
            return False
        return super().handle(car_type, engine_type)


class SUVRule(RuleHandler):
    def handle(self, car_type, engine_type):
        if car_type == "SUV" and engine_type == "Electric":
            print(f"Rule Violation: SUV cannot have Electric engine.")
            return False
        return super().handle(car_type, engine_type)


class SedanRule(RuleHandler):
    def handle(self, car_type, engine_type):
        # Sedans can have any engine, so just pass through
        return super().handle(car_type, engine_type)
