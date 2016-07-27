import unittest

from sharpshapes import *

class TestSharp(unittest.TestCase):

    def test_rect_area(self):
        rect = Rect(4, 5)
        self.assertEqual(rect.calculate_space(), 20)

    def test_circle_area(self):
        circle = Circle(4)
        self.assertEqual(circle.calculate_space(), 50.26544)

    def test_cuboid_volume(self):
        cuboid = Cuboid(2, 3, 4)
        self.assertEqual(cuboid.calculate_space(), 24)

    def test_cylinder_volume(self):
        cylinder = Cylinder(4, 10)
        self.assertEqual(cylinder.calculate_space(), 502.6544)


if __name__ == '__main__':
    unittest.main()
