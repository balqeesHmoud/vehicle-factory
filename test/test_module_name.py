import unittest
from module_name.motorcycle import Motorcycle
from module_name.car import Car
from module_name.factory import Factory

class TestVehicleFactory(unittest.TestCase):
    def test_motorcycle_creation(self):
        m = Motorcycle("ModelX", "petrol")
        self.assertEqual(m.get_model_name(), "ModelX")
        self.assertEqual(m.get_fuel_type(), "petrol")
        self.assertEqual(Factory.get_total_motorcycles(), 1)

    def test_car_creation(self):
        c = Car("ModelY", "diesel", "red", 4)
        self.assertEqual(c.get_model_name(), "ModelY")
        self.assertEqual(c.get_fuel_type(), "diesel")
        self.assertEqual(c.get_color(), "red")
        self.assertEqual(c.get_number_of_doors(), 4)
        self.assertEqual(Factory.get_total_cars(), 1)

    def test_motorcycle_fuel_type_validation(self):
        m = Motorcycle("ModelZ", "electric")
        with self.assertRaises(ValueError):
            m.set_fuel_type("hydrogen")

    def test_car_number_of_doors_validation(self):
        c = Car("ModelA", "petrol", "blue", 4)
        with self.assertRaises(ValueError):
            c.set_number_of_doors(3)

if __name__ == "__main__":
    unittest.main()
