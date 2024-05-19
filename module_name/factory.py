from abc import ABC, abstractmethod

class Factory(ABC):
    _total_cars = 0
    _total_motorcycles = 0

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    def increment_cars(cls):
        cls._total_cars += 1

    @classmethod
    def increment_motorcycles(cls):
        cls._total_motorcycles += 1

    @classmethod
    def get_total_cars(cls):
        return cls._total_cars

    @classmethod
    def get_total_motorcycles(cls):
        return cls._total_motorcycles
