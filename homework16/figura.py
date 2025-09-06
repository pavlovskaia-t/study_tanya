from abc import ABC, abstractmethod
import math
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass
class Square(Figura):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimetr(self):
        return self.__side * 4
class Rectangle(Figura):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimetr(self):
        return 2 * (self.__width + self.__height)

class Circle(Figura):
    def __init__(self, radius):
        self.__radius = radius  # приватный атрибут

    def area(self):
        return math.pi * self.__radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.__radius
shapes = [Square(5), Rectangle(3,7), Circle(4)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: Площа = {shape.area()}, Периметр = {shape.perimetr()}")
