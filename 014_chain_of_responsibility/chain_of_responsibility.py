class Car:
    def __init__(self, name: str, water: int, fuel: int, oil: int):
        """
        :rtype: None
        :param name: string
        :param water: int
        :param fuel: int
        :param oil: int
        """
        self.name = name
        self.water = water
        self.fuel = fuel
        self.oil = oil

    def is_fine(self) -> bool:
        if self.water >= 20 and self.fuel >= 5 and self.oil >= 10:
            print('Car is fine')
            return True
        else:
            print('Something wrong with car')
            return False


class Handler:
    def __init__(self, successor: object = None) -> object:
        """
        :type successor: object
        """
        self._handler = successor

    def handle_request(self, car_to_fix: Car):
        """
        :type car_to_fix: Car
        """
        if not car_to_fix.is_fine() and self._handler is not None:
            self._handler.handle_request(car_to_fix)


class WaterHandler(Handler):
    def handle_request(self, car_to_fix: Car) -> object:
        """
        :rtype: None
        :param car_to_fix: Car
        """
        if car_to_fix.water < 20:
            car_to_fix.water = 100
            print('Added water')
        super().handle_request(car_to_fix)


class FuelHandler(Handler):
    def handle_request(self, car_to_fix: Car) -> object:
        """
        :type car_to_fix: Car
        """
        if car_to_fix.fuel < 5:
            car_to_fix.fuel = 100
            print('Fuel added')
        super().handle_request(car_to_fix)


class OilHandler(Handler):
    def handle_request(self, car_to_fix: Car) -> object:
        """
        :type car_to_fix: Car
        """
        if car_to_fix.oil < 10:
            car_to_fix.oil = 100
            print('Oil was added')
        super().handle_request(car_to_fix)


garage_handler = OilHandler(FuelHandler(WaterHandler()))

car = Car('my car', 1, 1, 1)

garage_handler.handle_request(car)
