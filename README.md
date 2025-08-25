# car_factory # initial commit
This is a project that implements a simplified car factory that simulates the creation and management of cars with specific rules. This project was worked on by Ubi Precious and Yusra Adeyeri

# Design Pattern In Object Oriented Programming.
Design pattern is a proven, reusable solution to a common problem that occurs in software design. They are like templates or blueprints (not finished code), which guides how to structure classes and objects to solve specific recurring problems.

# Why use design patterns.
1. They promote reusability
2. they improve communication
3. They make code flexible and maintainable

# Categories of design patterns.
The famous "Gang of Four" (GoF) book groups them into three(3) main categories:

1. Creational Patterns - How to create objects.
    - Singleton: Only one instance of a class (e.g app configuration, database connection).
    - Factory Method: Creates objects without specifying exact class.
    - Abstract Factory: Factory of factories.
    - Builder: Step-by-step object construction.
    - Prototype: Cloning existing objects.

2. Structural Patterns - How to compose classes/objects.
    - Adapter: Make incompatible interfaces work together.
    - Decorator: Add new behaviour to an object dynamically.
    - Composite: Treat individual and group objects the same way.
    - Facade: Provide a simple interface to a complex system.
    - Proxy: Control access to another object.

3. Behavioral Patterns - How objects communicate.
    - Observer: Notify multiple objects when something changes.
    - Strategy: Swap algorithms at runtime.
    - Command: Encapsulate a request as an object.
    - Chain of responsibility: Passes a request along a chain of handlers.
    - Iterator: Traverses elements in a collection.

# Project Structure
car_factory/
|- car.py           # Car base class and implementation
|- factory.py       # CarFactory (Factory Method)
|- management.py    # CarManager (Singleton)
|- main.py          # Example usage

# first commit
The first commit makes use of the Factory Method (Car types) and the Singleton (Production Management) because they are the most fundamental design pattern to car production.
1. Factory Method - for creating different car types (Sedan, SUV, SportsCar).
2. Singleton - CarManager ensures a single point of control for production and state management.
3. Basic Car Functions - Clear separation of components (engine, music, gear etc).