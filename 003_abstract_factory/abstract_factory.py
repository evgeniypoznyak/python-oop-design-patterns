# === abstract shape classes ===
class Shape2DInterface:
    def draw(self): pass


class Shape3DInterface:
    def build(self): pass


class TouchInterface:
    def touch(self): pass


# === concrete shape classes ===
class Circle(Shape2DInterface):
    def draw(self):
        print('Circle.draw')


class Square(Shape2DInterface):
    def draw(self):
        print('Square.draw')


class Sphere(Shape3DInterface):
    def build(self):
        print('Sphere.build')


class Slide(TouchInterface, Shape3DInterface):
    def touch(self):
        print('touching the Slide')

    def build(self):
        print('building the Slide...')


class Panel(TouchInterface, Shape2DInterface):
    def touch(self):
        print('touching the Panel')

    def draw(self):
        print('Drawing the Panel')


class Cube(Shape3DInterface):
    def build(self):
        print('Cube.build')


# === Abstract shape factory ===
class ShapeFactoryInterface:
    def getShape(sides): pass


# === Concrete shape factories ===
class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, 'Bad 2D shape creation: shape factory not defined for ' + sides + ' sides'


class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        """ here, sides refers to the number faces"""
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, 'Bad 3D shape creation: shape factory not defined for ' + sides + ' sides'


class ShapeTouchFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Slide()
        if sides == 2:
            return Panel()
        assert 0, 'Bad touch request: shape factory is not defined for ' + sides + ' sides'


shape2DFactory = Shape2DFactory()
circle = shape2DFactory.getShape(1)
print(circle)
circle.draw()

shape3DFactory = Shape3DFactory()
sphere = shape3DFactory.getShape(1)
print(sphere)
sphere.build()


touchFactory = ShapeTouchFactory()
slide = ShapeTouchFactory.getShape(1)
slide.touch()
slide.build()

panel = ShapeTouchFactory.getShape(2)
panel.touch()
panel.draw()