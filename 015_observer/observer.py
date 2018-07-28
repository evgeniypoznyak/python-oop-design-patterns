class Observable:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class Observer:
    def update(self, *args, **kwargs): pass


class AmericanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print(f'American stock market recieved: {args} | {kwargs}')


class EuropeanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print(f'European stock market recieved: {args} | {kwargs}')


market = Observable()

american = AmericanStockMarket()
market.register(american)

european = EuropeanStockMarket()
market.register(european)

market.update_observers('Subject of message: ', msg='Message from observable')