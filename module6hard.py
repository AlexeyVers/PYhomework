from math import pi
class Figure:
    sides_count = 0
    def __init__(self, __sides, __color, filled):
        self.__sides = []
        self.__color = []
        self.filled = bool

    def get_color(self):
        return self._color

    def __is_valid_color(*args):
        valid_color = True
        for i in args[1]:
            if i > 255:
                valid_color = False
                print('Некорректно введён цвет')
        return valid_color

    def set_color(self, *args):
        if self.__is_valid_color(args):
            self._color = args

    def __is_valid_sides(self, sides):
        valid_sides = True
        for i in sides:
            if isinstance(i) != int and isinstance(i) > 0:
                valid_sides = False
                return valid_sides
        if valid_sides and len(sides) == len(self._sides):
            valid_sides = True
            return valid_sides
        else:
            valid_sides = False
            return valid_sides

    def get_sides(self):
        return self._sides
    def __len__(self):
        _len = 0
        if self.sides_count == 1:
            _len = int((float(self._sides[0])) * pi)
            return _len
        elif self.sides_count == 3:
            _len = (self._sides ** 2) / 2
            return _len
        elif self.sides_count == 12:
            _len = self._sides ** 3
            return _len

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self._sides = [*new_sides]

class Circle(Figure):
    sides_count = 1
    def __init__(self, _color, _sides):
        self._color = _color
        self._sides = _sides
        self.radius = _sides / (pi * 2)

    def get_square(self):
        square = (self.__radius(self) ** 2) * pi
        return square

class Triangle(Figure):
    sides_count = 3

    def __init__(self, _color, _sides):
        self._color = _color
        self._sides = _sides

    def get_square(self):
        p = (self._sides[0] + self._sides[1] + self._sides[2]) / 2
        square = (p * (p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2])//2)
        return square

class Cube(Figure):
    sides_count = 12

    def __init__(self, _color, _sides):
        self._color = _color
        sides = []
        for i in range(0,11):
            sides.append(_sides)
        self._sides = sides

    def get_volume(self):
        volume = self._sides[0] ** 3
        return volume


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
