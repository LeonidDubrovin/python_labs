import matplotlib.pyplot as plt
import random
import math
import uuid
import numpy as np


class Factory:
    objects = []
    JobMode = ['AddObj', 'GenObj', 'DelObj', 'IsIntersect', 'CompareArea', 'MoveObj', 'DrawObj', 'Exit']

    def choose_object(self):
        show_objects()
        item = Menu.select_item(len(self.objects)) - 1
        obj = self.objects[item]
        return obj

    def add_object(self, obj):
        self.objects.append(obj)

    def del_object(self, obj):
        del self.objects[self.objects.index(obj)]

    @staticmethod
    def new_triangle():
        new_obj = Triangle()
        while True:
            tmp_arr = []
            i = 0
            while i < new_obj.num_coord:
                p = try_input_point(f"{i} (x,y): ")
                tmp_arr.append(p)
                i += 1
            if new_obj.is_triangle(tmp_arr):
                new_obj.set_coordinates(tmp_arr)
                break
            else:
                raise ValueError("Нельзя построить треугольник по данным точкам")
        return new_obj

    @staticmethod
    def new_quadrate():
        new_obj = Quadrate()
        tmp_arr = []
        while True:
            i = 0
            while i < new_obj.num_coord:
                p = try_input_point(f"{i} (x,y): ")
                tmp_arr.append(p)
                i += 1
            if new_obj.is_quadrate(tmp_arr):
                new_obj.set_coordinates(tmp_arr)
                break
            raise ValueError("Нельзя построить квадрат по данным точкам")
        return new_obj

    @staticmethod
    def new_rectangle():
        new_obj = Rectangle()
        tmp_arr = []
        while True:
            i = 0
            while i < new_obj.num_coord:
                p = try_input_point(f"{i} (x,y): ")
                tmp_arr.append(p)
                i += 1
            if new_obj.is_rectangle(tmp_arr):
                new_obj.set_coordinates(tmp_arr)
                break
            raise ValueError("Нельзя построить прямоугольник по данным точкам")
        return new_obj

    @staticmethod
    def new_pentagon():
        new_obj = Pentagon()
        tmp_arr = []
        while True:
            i = 0
            while i < new_obj.num_coord:
                p = try_input_point(f"{i} (x,y): ")
                tmp_arr.append(p)
                i += 1
            if new_obj.is_pentagon(tmp_arr):
                new_obj.set_coordinates(tmp_arr)
                break
            raise ValueError("Нельзя построить пятиугольник по данным точкам")
        return new_obj

    @staticmethod
    def is_intersect(obj1, obj2):
        is_objects_intersect = False
        counter = 0
        for p in obj1.coordinates:
            if obj2.is_dot_in_figure(p):
                counter += 1
        if 0 < counter < len(obj1.coordinates):
            is_objects_intersect = True

        if is_objects_intersect is False:
            counter = 0
            for p in obj2.coordinates:
                if obj1.is_dot_in_figure(p):
                    counter += 1
                if 0 < counter < len(obj2.coordinates):
                    is_objects_intersect = True
        return is_objects_intersect


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    def __init__(self):
        self.coordinates = []
        self.id = uuid.uuid4()

    def set_coordinates(self, coord):
        self.coordinates = coord

    def move(self, mov):
        for c in self.coordinates:
            c.x += mov.x
            c.y += mov.y

    def draw(self):
        for i, p in enumerate(self.coordinates):
            plt.scatter(p.x, p.y, s=35)
            if i == len(self.coordinates) - 1:
                plt.plot([self.coordinates[i].x, self.coordinates[0].x], [self.coordinates[i].y, self.coordinates[0].y],
                         'k-', lw=2)
            else:
                plt.plot([self.coordinates[i].x, self.coordinates[i + 1].x],
                         [self.coordinates[i].y, self.coordinates[i + 1].y], 'k-', lw=2)
        plt.xlabel("x", fontsize=10)
        plt.ylabel("y", fontsize=10)
        plt.tick_params(axis='both', which='major', labelsize=9)
        plt.axis('equal')
        plt.show()

    def is_dot_in_figure(self, point: Point) -> bool:
        s = 0
        for i in range(len(self.coordinates)):
            tr = Triangle()
            tmp_arr = []
            if i == len(self.coordinates) - 1:
                tmp_arr.append(Point(self.coordinates[0].x, self.coordinates[0].y))
                tmp_arr.append(Point(self.coordinates[i].x, self.coordinates[i].y))
            else:
                tmp_arr.append(Point(self.coordinates[i].x, self.coordinates[i].y))
                tmp_arr.append(Point(self.coordinates[i + 1].x, self.coordinates[i + 1].y))
            tmp_arr.append(point)
            tr.set_coordinates(tmp_arr)
            s += tr.get_area()
        if math.isclose(s, self.get_area()):
            return True
        else:
            return False


class Triangle(Figure):
    num_coord = 3

    def __init__(self):
        super().__init__()

    @staticmethod
    def is_triangle(coords):
        p1, p2, p3 = coords
        tmp = (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))
        if tmp != 0:
            return True
        else:
            return False

    def generate_coordinates(self):
        while True:
            p1 = Point(random.randint(2, 15), random.randint(2, 15))
            p2 = Point(random.randint(2, 15), random.randint(2, 15))
            vect = (p2.x - p1.x, p2.y - p1.y)
            p3 = Point(p1.x - vect[1], p1.y + vect[0])
            if self.is_triangle([p1, p2, p3]):
                self.coordinates.append(p1)
                self.coordinates.append(p2)
                self.coordinates.append(p3)
                break

    def get_area(self):
        p1, p2, p3 = self.coordinates
        a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
        b = math.sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)
        c = math.sqrt((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2)
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area


class Quadrate(Figure):
    num_coord = 4

    def __init__(self):
        super().__init__()

    @staticmethod
    def dist_sq(p: Point, q: Point):
        return (p.x - q.x) ** 2 + (p.y - q.y) ** 2

    @staticmethod
    def is_quadrate(coords) -> bool:
        p1, p2, p3, p4 = coords
        d2 = Quadrate.dist_sq(p1, p2)
        d3 = Quadrate.dist_sq(p1, p3)
        d4 = Quadrate.dist_sq(p1, p4)

        if d2 == 0 or d3 == 0 or d4 == 0:
            return False
        if d2 == d3 and 2 * d2 == d4 and 2 * Quadrate.dist_sq(p2, p4) == Quadrate.dist_sq(p2, p3):
            return True
        if d3 == d4 and 2 * d3 == d2 and 2 * Quadrate.dist_sq(p3, p2) == Quadrate.dist_sq(p3, p4):
            return True
        if d2 == d4 and 2 * d2 == d3 and 2 * Quadrate.dist_sq(p2, p3) == Quadrate.dist_sq(p2, p4):
            return True
        return False

    def generate_coordinates(self):
        p1 = Point(random.randint(2, 15), random.randint(2, 15))
        p2 = Point(random.randint(2, 15), random.randint(2, 15))
        vect = (p2.x - p1.x, p2.y - p1.y)
        p3 = Point(p2.x - vect[1], p2.y + vect[0])
        p4 = Point(p1.x - vect[1], p1.y + vect[0])
        self.coordinates.append(p1)
        self.coordinates.append(p2)
        self.coordinates.append(p3)
        self.coordinates.append(p4)

    def get_area(self):
        p1, p2, p3, p4 = self.coordinates
        area = (vector_length(p1, p2)) ** 2
        return area


class Rectangle(Figure):
    num_coord = 4

    def __init__(self):
        super().__init__()

    @staticmethod
    def is_rectangle(coords):
        p1, p2, p3, p4 = coords
        return ((p2.x - p1.x) * (p3.x - p2.x) + (p2.y - p1.y) * (p3.y - p2.y)) == 0 and (
                    (p2.x - p1.x) * (p4.x - p1.x) + (p2.y - p1.y) * (p4.y - p1.y)) == 0

    def generate_coordinates(self):
        p1 = Point(random.randint(2, 15), random.randint(2, 15))
        p2 = Point(random.randint(2, 15), random.randint(2, 15))
        vect = [p2.x - p1.x, p2.y - p1.y]
        val = random.random() * 2
        vect[0] *= val
        vect[1] *= val
        p3 = Point(p2.x - vect[1], p2.y + vect[0])
        p4 = Point(p1.x - vect[1], p1.y + vect[0])
        self.coordinates.append(p1)
        self.coordinates.append(p2)
        self.coordinates.append(p3)
        self.coordinates.append(p4)

    def get_area(self):
        p1, p2, p3, p4 = self.coordinates

        ab = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        bc = math.sqrt((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2)
        return ab * bc


class Pentagon(Figure):
    num_coord = 5

    def __init__(self):
        super().__init__()

    @staticmethod
    def is_pentagon(coords):
        is_pentagon_object = True
        for i in range(0, len(coords)):
            if i == len(coords) - 1:
                vec1 = [coords[i-1].x - coords[i].x, coords[i-1].y - coords[i].y]
                vec2 = [coords[0].x - coords[i].x, coords[0].y - coords[i].y]
            else:
                vec1 = [coords[i-1].x - coords[i].x, coords[i-1].y - coords[i].y]
                vec2 = [coords[i+1].x - coords[i].x, coords[i+1].y - coords[i].y]
            unit_vector_1 = vec1 / np.linalg.norm(vec1)
            unit_vector_2 = vec2 / np.linalg.norm(vec2)
            dot_product = np.dot(unit_vector_1, unit_vector_2)
            angle_rad = np.arccos(dot_product)
            angle = np.degrees(angle_rad)
            if not math.isclose(angle, 108):
                is_pentagon_object = False
        return is_pentagon_object

    def generate_coordinates(self):
        pentagon = []
        R = random.randint(8, 15)
        start_rad = random.randint(0, 90)
        for n in range(0, 5):
            x = R * math.cos(math.radians(start_rad + n * 72))
            y = R * math.sin(math.radians(start_rad + n * 72))
            pentagon.append(Point(x, y))
        self.coordinates = pentagon

    def get_area(self):
        p1, p2, p3, p4, p5 = self.coordinates
        a = vector_length(p1, p2)
        area = (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * a * a) / 4
        return area

    def is_dot_in_figure(self, point):
        result = False
        j = len(self.coordinates) - 1
        for i in range(len(self.coordinates)):
            cond1 = (self.coordinates[i].y < point.y and self.coordinates[j].y >= point.y
                     or self.coordinates[j].y < point.y and self.coordinates[i].y >= point.y)
            cond2 = (self.coordinates[i].x + (point.y - self.coordinates[i].y) / (
                        self.coordinates[j].y - self.coordinates[i].y) *
                     (self.coordinates[j].x - self.coordinates[i].x) < point.x)
            if cond1 and cond2:
                result = not result
            j = i
        return result


def vector_length(point1: Point, point2: Point):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def draw_objects():
    plt.xlabel("x", fontsize=10)
    plt.ylabel("y", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=9)
    plt.axis('equal')
    plt.show()


def add_obj_to_show(obj):
    for i, p in enumerate(obj.coordinates):
        plt.scatter(p.x, p.y, s=35)
        if i == len(obj.coordinates) - 1:
            plt.plot([obj.coordinates[i].x, obj.coordinates[0].x], [obj.coordinates[i].y, obj.coordinates[0].y], 'k-',
                     lw=2)
        else:
            plt.plot([obj.coordinates[i].x, obj.coordinates[i + 1].x], [obj.coordinates[i].y, obj.coordinates[i + 1].y],
                     'k-', lw=2)


def try_input_point(string: str) -> Point:
    while True:
        try:
            x, y = input(string).split()
            return Point(float(x), float(y))
        except ValueError:
            print("Ошибка при вводе")


def show_objects():
    for i, obj in enumerate(Factory.objects):
        print("{}) {}, {}: ".format(i + 1, type(obj).__name__, obj.id))


class Menu:
    @staticmethod
    def select_item(n_item) -> int:
        while True:
            try:
                item = (input(f"Ввдеите комманду (число 1-{n_item}): "))
                if 0 < int(item) <= n_item:
                    return int(item)
                else:
                    print("Неправильное число")
            except ValueError:
                print("Ошибка при вводе числа")

    @staticmethod
    def select():
        menu_items = {
            1: 'Добавить',
            2: 'Сгенерировать объекты',
            3: 'Удалить',
            4: 'Определить пересекаются ли объекты',
            5: 'Сравнить площади объектов',
            6: 'Передвинуть объект',
            7: 'Нарисовать объект',
            8: 'Выход',
        }
        print(30 * "-", "МЕНЮ", 30 * "-")
        for key in menu_items:
            print('{0}){1}'.format(key, menu_items[key]))
        print(66 * "-")
        item = Menu.select_item(len(menu_items)) - 1
        return Factory.JobMode[item]


def main():
    factory = Factory()
    job_mode = Menu.select()
    try:
        while job_mode != 'Exit':
            menu_figures = {
                1: 'Triangle',
                2: 'Quadrate',
                3: 'Rectangle',
                4: 'Pentagon'
            }
            if job_mode == 'AddObj':
                for key in menu_figures:
                    print('{0}){1}'.format(key, menu_figures[key]))
                item = Menu.select_item(len(menu_figures))
                new_obj = None
                if item == 1:
                    print("Введите координаты треугольника")
                    new_obj = Factory.new_triangle()
                    if new_obj:
                        print("Треугольник добавлен")

                elif item == 2:
                    print("Введите координаты квадрата")
                    new_obj = Factory.new_quadrate()
                    if new_obj:
                        print("Квадрат добавлен")
                elif item == 3:
                    new_obj = Factory.new_rectangle()
                    if new_obj:
                        print("Прямоугольник добавлен")
                elif item == 4:
                    new_obj = Factory.new_pentagon()
                    if new_obj:
                        print("Пятиугольник добавлен")
                factory.add_object(new_obj)
            elif job_mode == 'GenObj':
                for key in menu_figures:
                    print('{0}){1}'.format(key, menu_figures[key]))
                item = Menu.select_item(len(menu_figures))
                new_obj = None
                if item == 1:
                    new_obj = Triangle()
                elif item == 2:
                    new_obj = Quadrate()
                elif item == 3:
                    new_obj = Rectangle()
                elif item == 4:
                    new_obj = Pentagon()
                new_obj.generate_coordinates()
                factory.add_object(new_obj)
                print("Объект сгенерирован, тип: ", type(new_obj).__name__)

            elif job_mode == 'DelObj':
                if len(factory.objects):
                    print("Какой объект удалить?")
                    obj = factory.choose_object()
                    factory.del_object(obj)
                    print("Объект удален")
                else:
                    print("Нет объектов")
            elif job_mode == 'IsIntersect':
                print("Выберите первый объект для определения пересечения")
                obj1 = factory.choose_object()
                print("Выберите второй объект для определения пересечения")
                obj2 = factory.choose_object()
                if obj1 is not obj2:
                    if factory.is_intersect(obj1, obj2):
                        print("Объекты пересекаются")
                    else:
                        print("Объекты не пересекаются")
                    add_obj_to_show(obj1)
                    add_obj_to_show(obj2)
                    draw_objects()
                else:
                    print("Нельзя сравнивать объект с самим собой")
            elif job_mode == 'MoveObj':
                if len(factory.objects):
                    print("Какой объект передвинуть?")
                    obj = factory.choose_object()
                    print("Координаты для передвижения")
                    x, y = input(f"(x,y): ").split()
                    x, y = float(x), float(y)
                    factory.objects[factory.objects.index(obj)].move(Point(x, y))
                else:
                    print("Нет объектов")
            elif job_mode == 'CompareArea':
                if len(factory.objects) >= 2:
                    print("Выберите первый объект для сравнения площади")
                    obj1 = factory.choose_object()
                    print("Выберите второй объект для сравнения площади")
                    obj2 = factory.choose_object()
                    obj1_area = obj1.get_area()
                    obj2_area = obj2.get_area()
                    if obj1_area > obj2_area:
                        print("Площадь первого больше площади второго: {} > {}".format(obj1_area, obj2_area))
                    elif obj1_area < obj2_area:
                        print("Площадь первого меньше площади второго: {} < {}".format(obj1_area, obj2_area))
                    else:
                        print("Площади одинаковы: {} = {}".format(obj1_area, obj2_area))

                else:
                    print("Меньше двух объектов")

            elif job_mode == 'DrawObj':
                if len(factory.objects):
                    print("Какой объект рисовать?")
                    obj = factory.choose_object()
                    obj.draw()
                else:
                    print("Нет объектов")
            job_mode = Menu.select()
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
