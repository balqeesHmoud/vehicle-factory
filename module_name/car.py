from module_name.factory import Factory

class Car(Factory):
    def __init__(self, model_name, fuel_type, color, number_of_doors):
        self._number_of_wheels = 4
        self._model_name = model_name
        self._fuel_type = fuel_type
        self._color = color
        self._number_of_doors = number_of_doors
        Factory.increment_cars()

    def set_model_name(self, model_name):
        self._model_name = model_name

    def set_fuel_type(self, fuel_type):
        if fuel_type in ["electric", "petrol", "diesel"]:
            self._fuel_type = fuel_type
        else:
            raise ValueError("Invalid fuel type. Choose either 'electric', 'petrol', or 'diesel'.")

    def set_color(self, color):
        self._color = color

    def set_number_of_doors(self, number_of_doors):
        if number_of_doors in [2, 4]:
            self._number_of_doors = number_of_doors
        else:
            raise ValueError("Invalid number of doors. Choose either 2 or 4.")

    def get_model_name(self):
        return self._model_name

    def get_fuel_type(self):
        return self._fuel_type

    def get_color(self):
        return self._color

    def get_number_of_doors(self):
        return self._number_of_doors

    def __str__(self):
        return (f"Car(model_name={self._model_name}, fuel_type={self._fuel_type}, "
                f"color={self._color}, number_of_doors={self._number_of_doors}, "
                f"number_of_wheels={self._number_of_wheels})")
