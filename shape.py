PI = 3.14159

class Shape(object):
    '''The base Shape class with placeholder attributes'''
    required_args = []

    def calculate_space(self):
        return -1

    def __str__(self):
        return 'Undefined shape.'


class Rect(Shape):
    required_args = ['width', 'height']

    def __init__(self, width, height):
        self.width, self.height = width, height

    def calculate_space(self):
        return self.width * self.height

    def __str__(self):
        return 'The total area of the rectangle is {}'.format(self.calculate_space())


class Circle(Shape):
    required_args = ['radius']

    def __init__(self, radius):
        self.radius = radius

    def calculate_space(self):
        return PI * self.radius ** 2

    def __str__(self):
        return 'The total area of the circle is {}'.format(self.calculate_space())


class Cuboid(Shape):
    required_args = ['width', 'height', 'depth']

    def __init__(self, width, height, depth):
        self.width, self.height, self.depth = width, height, depth

    def calculate_space(self):
        return self.width * self.height * self.depth

    def __str__(self):
        return 'The total volume of the cuboid is {}'.format(self.calculate_space())


class Cylinder(Shape):
    required_args = ['radius', 'height']

    def __init__(self, radius, height):
        self.radius, self.height = radius, height

    def calculate_space(self):
        return PI * self.radius ** 2 * self.height

    def __str__(self):
        return 'The total volume of the cylinder is {}'.format(self.calculate_space())
