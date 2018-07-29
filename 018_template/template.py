class MakeMeal:
    def buy_ingredients(self, money):
        if money < self.cost:
            assert 0, 'Not enough money'

    def prepare(self):
        pass

    def cook(self):
        pass

    def go(self, money):
        self.buy_ingredients(money)
        self.prepare()
        self.cook()


class MakePizza(MakeMeal):
    def __init__(self):
        self.cost = 3

    def prepare(self):
        print('Prepare pizza...')

    def cook(self):
        print('Cooking the pizza...')


class MakeCake(MakeMeal):
    def __init__(self):
        self.cost = 2

    def prepare(self):
        print('Prepare cake...')

    def cook(self):
        print('Making the cake...')



p = MakePizza()
p.go(3)

c = MakeCake()
c.go(3)
