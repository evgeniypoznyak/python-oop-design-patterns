class ShapeInterface:
    def draw(self): pass


class Circle(ShapeInterface):
    def draw(self):
        print('Circle.draw')


class Square(ShapeInterface):
    def draw(self):
        print('Square.draw')


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Square()
        else:
            assert 0, 'Could not find shape ' + type


shapeFactory = ShapeFactory()
square = shapeFactory.getShape('square')
circle = shapeFactory.getShape('circle')
# poop = shapeFactory.getShape('poop')

square.draw()
circle.draw()
