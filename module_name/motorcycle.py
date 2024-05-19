from module_name.factory import Factory

class Motorcycle(Factory):
    def __init__(self, model_name, fuel_type):
        self._number_of_wheels = 2
        self._model_name = model_name
        self._fuel_type = fuel_type
        Factory.increment_motorcycles()

    def set_model_name(self, model_name):
        self._model_name = model_name

    def set_fuel_type(self, fuel_type):
        if fuel_type in ["electric", "petrol", "diesel"]:
            self._fuel_type = fuel_type
        else:
            raise ValueError("Invalid fuel type. Choose either 'electric', 'petrol', or 'diesel'.")

    def get_model_name(self):
        return self._model_name

    def get_fuel_type(self):
        return self._fuel_type

    def __str__(self):
        return f"Motorcycle(model_name={self._model_name}, fuel_type={self._fuel_type}, number_of_wheels={self._number_of_wheels})"
