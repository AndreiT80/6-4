import math


class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled = True):
        self.__sides = [sides for i in range(self.sides_count)]
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        '''Метод get_color, возвращает список RGB цветов.'''
        return self.__color

    def __is_valid_color(self, r, g, b):
        '''Метод __is_valid_color - служебный, принимает параметры r, g, b, который
         проверяет корректность переданных значений перед установкой нового цвета. Корректным
         цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).'''
        return True if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 else False

    def set_color(self, r, g, b):
        '''Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на
        cоответствующие значения, предварительно проверив их на корректность. Если введены
         некорректные данные, то цвет остаётся прежним.'''
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        '''Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
         возвращает True если все стороны целые положительные числа и кол-во новых сторон
         совпадает с текущим, False - во всех остальных случаях.'''
        for side in sides:
            if side > 0 and isinstance(side, int) and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        '''Метод get_sides должен возвращать значение я атрибута __sides.'''
        return self.__sides

    def __len__(self):
        '''Метод __len__ должен возвращать периметр фигуры.'''
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        '''Метод set_sides(self, *new_sides) должен принимать новые стороны, если их
        количество не равно sides_count, то не изменять, в противном случае - менять.'''
        list_new_sides = [*new_sides]
        if self.__is_valid_sides(list_new_sides) is True:
           self.__sides = list_new_sides

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / 2 * math.pi

    def get_square(self):
        return self.__radius ** 2 * math.pi


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
        self.__a = self.__sides[0]
        self.__b = self.__sides[1]
        self.__c = self.__sides[2]

    def get_square(self):
        a = self.__a
        b = self.__b
        c = self.__c
        p = 0.5 * (a + b + c)
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
    def get_volume(self):
        v = self.__sides ** 3
        return v


circle1 = Circle((200, 200, 100), 10)   # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)              # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)               # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)           # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)                               # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())