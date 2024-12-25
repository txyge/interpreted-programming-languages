class ShapeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Pentagon:
    def __init__(self, identifier, side_length, x=0, y=0):
        if side_length <= 0:
            raise ShapeError("Длина стороны должна быть положительной.")
        self.identifier = identifier
        self.side_length = side_length
        self.x = x
        self.y = y

    def area(self):
        # Площадь правильного пятиугольника
        return (5 * self.side_length ** 2) / (4 * (1 / (2 * (5 ** 0.5))) ** 0.5)

    def get_vertices(self):
        # Получение вершин пятиугольника
        angle = 2 * 3.14159 / 5
        return [(self.x + self.side_length * cos(i * angle),
                 self.y + self.side_length * sin(i * angle)) for i in range(5)]

    def is_intersect(self, triangle):
        # Проверка пересечения пятиугольника с треугольником
        pentagon_vertices = self.get_vertices()
        triangle_vertices = triangle.get_vertices()

        # Проверка всех ребер пятиугольника на пересечение с ребрами треугольника
        for i in range(len(pentagon_vertices)):
            for j in range(len(triangle_vertices)):
                if self.segments_intersect(pentagon_vertices[i], pentagon_vertices[(i + 1) % 5],
                                            triangle_vertices[j], triangle_vertices[(j + 1) % 3]):
                    return True
        return False

    def segments_intersect(self, p1, p2, p3, p4):
        # Проверка пересечения отрезков p1p2 и p3p4
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0  # collinear
            return 1 if val > 0 else 2  # clock or counterclock wise

        o1 = orientation(p1, p2, p3)
        o2 = orientation(p1, p2, p4)
        o3 = orientation(p3, p4, p1)
        o4 = orientation(p3, p4, p2)

        # Общий случай
        if o1 != o2 and o3 != o4:
            return True

        return False

class Triangle:
    def __init__(self, identifier, base, height, x=0, y=0):
        if base <= 0 or height <= 0:
            raise ShapeError("Основание и высота должны быть положительными.")
        self.identifier = identifier
        self.base = base
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return 0.5 * self.base * self.height

    def get_vertices(self):
        # Получение вершин треугольника
        return [(self.x, self.y), 
                (self.x + self.base, self.y), 
                (self.x + self.base / 2, self.y + self.height)]

    def is_intersect(self, pentagon):
        # Проверка пересечения треугольника с пятиугольником
        return pentagon.is_intersect(self)
def compare(shape1, shape2):
    """Сравнение двух фигур по площади."""
    area1 = shape1.area()
    area2 = shape2.area()
    if area1 > area2:
        return f"{shape1.identifier} больше {shape2.identifier}."
    elif area1 < area2:
        return f"{shape2.identifier} больше {shape1.identifier}."
    else:
        return "Площади равны."

from math import cos, sin, pi

try:
    pentagon = Pentagon("Pentagon1", 10, x=1, y=1)
    triangle = Triangle("Triangle1", 4, 3, x=2, y=2)

    print(f"Площадь пятиугольника: {pentagon.area()}")
    print(f"Площадь треугольника: {triangle.area()}")

    # Сравнение площадей
    print(compare(pentagon, triangle))

    # Проверка на пересечение
    if pentagon.is_intersect(triangle):
        print(f"{pentagon.identifier} и {triangle.identifier} пересекаются.")
    else:
        print(f"{pentagon.identifier} и {triangle.identifier} не пересекаются.")

except ShapeError as e:
    print(f"Ошибка: {e}")    