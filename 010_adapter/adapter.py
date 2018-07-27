# Adaptee (source) interface

class EuropeanSocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


# Target interface
class USASocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1


# Client
class AmericanKettle:
    __power = None

    def __init__(self, power):
        self.__power = power  # SocketInterface

    def boil(self):
        if self.__power.voltage() > 110:
            print('Fire!!!')
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print('Works!')
            else:
                print('No power')


class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


socket = EuropeanSocket()

outlet = AmericanKettle(socket)
outlet.boil()

adapter = Adapter(socket)
outlet = AmericanKettle(adapter)
outlet.boil()
