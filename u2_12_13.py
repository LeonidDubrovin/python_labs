import matplotlib.pyplot as plt
import random
import math


class Factory:
    objects = []
    JobMode = ['AddObj', 'GenObj', 'DelObj', 'IsIntersect', 'Compare', 'MoveObj', 'DrawObj', 'Exit']

    def _choose_object(self):
        try:
            for i, obj in enumerate(self.objects):
                print("{}) {}: ".format(i + 1, type(obj).__name__))
            item = Menu.select_item(len(self.objects)) - 1
            obj = self.objects[item]
            return obj
        except ValueError:
            print("Ошибка при выборе объекта")

    def add_object(self):
        print("1. Triangle")
        print("2. Quadrate")
        print("3. Rectangle")
        print("4. Pentagon")
        item = Menu.select_item(4)

        new_obj = None
        if item == 1:
            new_obj = Triangle()
        elif item == 2:
            new_obj = Quadrate()
        elif item == 3:
            new_obj = Rectangle()
        elif item == 4:
            new_obj = Pentagon()
        new_obj.set_coordinates()
        self.objects.append(new_obj)

    def gen_object(self):
        print("1. Triangle")
        print("2. Quadrate")
        print("3. Rectangle")
        print("4. Pentagon")
        item = Menu.select_item(4)

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
        self.objects.append(new_obj)
        print("Объект сгенерирован, тип: ", type(new_obj).__name__)

    def del_object(self):
        if len(self.objects):
            print("Какой объект удалить?")
            obj = self._choose_object()
            del self.objects[self.objects.index(obj)]
            print("Объект удален")
        else:
            print("Нет объектов")

    def is_intersect(self):
        pass

    def compare(self):
        if len(self.objects) >= 2:
            print("Выберите первый объект для сравнения площади")
            obj1 = self._choose_object()
            print("Выберите второй объект для сравнения площади")
            obj2 = self._choose_object()
            obj1_area = obj1.get_area()
            obj2_area = obj2.get_area()
            if obj1_area > obj2_area:
                print("Плохадь первого больше площади второго: {} > {}".format(obj1_area, obj2_area))
            elif obj1_area < obj2_area:
                print("Плохадь первого меньше площади второго: {} < {}".format(obj1_area, obj2_area))
            else:
                print("Плохади одинаковы: {} = {}".format(obj1_area, obj2_area))

        else:
            print("Меньше двух объектов")

    def move(self):
        if len(self.objects):
            print("Какой объект передвинуть?")
            obj = self._choose_object()
            print("Координаты для передвижения")
            x, y = input(f"(x,y): ").split()
            x, y = float(x), float(y)
            self.objects[self.objects.index(obj)].move((x, y))
        else:
            print("Нет объектов")

    def draw(self):
        if len(self.objects):
            print("Какой объект рисовать?")
            obj = self._choose_object()
            obj.draw()
        else:
            print("Нет объектов")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    coordinates = []

    def move(self, mov):
        for c in self.coordinates:
            c.x += mov[0]
            c.y += mov[1]


class Triangle(Figure):
    num_coord = 3
    _coordinates = []

    def __init__(self):
        pass

    @staticmethod
    def is_triangle(coords):
        p1, p2, p3 = coords
        tmp = (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))
        if tmp != 0:
            return True
        else:
            return False

    def set_coordinates(self):
        print("Введите координаты треугольника")
        while True:
            tmp_arr = []
            i = 0
            while i < self.num_coord:
                try:
                    x, y = input(f"{i} (x,y): ").split()
                    tmp_arr.append(Point(float(x), float(y)))
                    i += 1
                except ValueError:
                    print("Ошибка при вводе")
            if self.is_triangle(tmp_arr):
                print("Треугольник добавлен ")
                self._coordinates = tmp_arr
                break
            else:
                print("Нельзя построить трекгоьник по данным точкам")

    def generate_coordinates(self):
        while True:
            p1 = Point(random.randint(2, 15), random.randint(2, 15))
            p2 = Point(random.randint(2, 15), random.randint(2, 15))
            vect = (p2.x - p1.x, p2.y - p1.y)
            p3 = Point(p1.x - vect[1], p1.y + vect[0])
            if self.is_triangle([p1, p2, p3]):
                self._coordinates.append(p1)
                self._coordinates.append(p2)
                self._coordinates.append(p3)
                break

    def get_area(self):
        p1, p2, p3 = self._coordinates
        s = (p1 + p2 + p3) / 2
        area = (s * (s - p1) * (s - p2) * (s - p3)) ** 0.5
        return area

    def draw(self):
        p1, p2, p3 = self._coordinates
        plt.scatter(p1.x, p1.y, s=35)
        plt.scatter(p2.x, p2.y, s=35)
        plt.scatter(p3.x, p3.y, s=35)
        plt.plot([p1.x, p2.x], [p1.y, p2.y], 'k-', lw=2)
        plt.plot([p1.x, p3.x], [p1.y, p3.y], 'k-', lw=2)
        plt.plot([p2.x, p3.x], [p2.y, p3.y], 'k-', lw=2)

        plt.title(type(self).__name__, fontsize=19)
        plt.xlabel("x", fontsize=10)
        plt.ylabel("y", fontsize=10)
        plt.axis('equal')
        plt.show()


class Quadrate(Figure):
    num_coord = 4

    @staticmethod
    def dist_sq(p: Point, q: Point):
        return (p.x - q.x) ** 2 + (p.y - q.y) ** 2

    def is_quadrate(self, coords) -> bool:
        p1, p2, p3, p4 = coords
        d2 = self.dist_sq(p1, p2)
        d3 = self.dist_sq(p1, p3)
        d4 = self.dist_sq(p1, p4)

        if d2 == 0 or d3 == 0 or d4 == 0:
            return False
        if d2 == d3 and 2 * d2 == d4 and 2 * self.dist_sq(p2, p4) == self.dist_sq(p2, p3):
            return True
        if d3 == d4 and 2 * d3 == d2 and 2 * self.dist_sq(p3, p2) == self.dist_sq(p3, p4):
            return True
        if d2 == d4 and 2 * d2 == d3 and 2 * self.dist_sq(p2, p3) == self.dist_sq(p2, p4):
            return True
        return False

    def set_coordinates(self):
        print("Введите координаты квадрата")
        tmp_arr = []
        while True:
            i = 0
            while i < self.num_coord:
                try:
                    x, y = input(f"{i} (x,y): ").split()
                    tmp_arr.append(Point(float(x), float(y)))
                    i += 1
                except ValueError:
                    print("Ошибка при вводе")
            if self.is_quadrate(tmp_arr):
                self.coordinates = tmp_arr
                break

    def generate_coordinates(self):
        p1 = Point(random.randint(2, 15), random.randint(2, 15))
        p2 = Point(random.randint(2, 15), random.randint(2, 15))
        vect = (p2.x - p1.x, p2.y - p1.y)
        p3 = Point(p1.x - vect[1], p1.y + vect[0])
        p4 = Point(p2.x - vect[1], p2.y + vect[0])
        self.coordinates.append(p1)
        self.coordinates.append(p2)
        self.coordinates.append(p3)
        self.coordinates.append(p4)

    def draw(self):
        p1, p2, p3, p4 = self.coordinates
        plt.scatter(p1.x, p1.y, s=35)
        plt.scatter(p2.x, p2.y, s=35)
        plt.scatter(p3.x, p3.y, s=35)
        plt.scatter(p4.x, p4.y, s=35)
        plt.plot([p1.x, p2.x], [p1.y, p2.y], 'k-', lw=2)
        plt.plot([p1.x, p3.x], [p1.y, p3.y], 'k-', lw=2)
        plt.plot([p2.x, p4.x], [p2.y, p4.y], 'k-', lw=2)
        plt.plot([p3.x, p4.x], [p3.y, p4.y], 'k-', lw=2)

        plt.title(type(self).__name__, fontsize=19)
        plt.xlabel("x", fontsize=10)
        plt.ylabel("y", fontsize=10)
        plt.axis('equal')
        plt.show()


class Rectangle(Figure):
    num_coord = 4

    def set_coordinates(self):
        print("Введите функция не готова")
        pass

    def generate_coordinates(self):
        p1 = Point(random.randint(2, 15), random.randint(2, 15))
        p2 = Point(random.randint(2, 15), random.randint(2, 15))
        vect = [p2.x - p1.x, p2.y - p1.y]
        val = random.random() * 2
        vect[0] *= val
        vect[1] *= val
        p3 = Point(p1.x - vect[1], p1.y + vect[0])
        p4 = Point(p2.x - vect[1], p2.y + vect[0])
        self.coordinates.append(p1)
        self.coordinates.append(p2)
        self.coordinates.append(p3)
        self.coordinates.append(p4)

    def draw(self):
        p1, p2, p3, p4 = self.coordinates
        plt.scatter(p1.x, p1.y, s=35)
        plt.scatter(p2.x, p2.y, s=35)
        plt.scatter(p3.x, p3.y, s=35)
        plt.scatter(p4.x, p4.y, s=35)
        plt.plot([p1.x, p2.x], [p1.y, p2.y], 'k-', lw=2)
        plt.plot([p1.x, p3.x], [p1.y, p3.y], 'k-', lw=2)
        plt.plot([p2.x, p4.x], [p2.y, p4.y], 'k-', lw=2)
        plt.plot([p3.x, p4.x], [p3.y, p4.y], 'k-', lw=2)

        plt.title(type(self).__name__, fontsize=19)
        plt.xlabel("x", fontsize=10)
        plt.ylabel("y", fontsize=10)
        plt.axis('equal')
        plt.show()


class Pentagon(Figure):
    num_coord = 5

    def generate_coordinates(self):
        pentagon = []
        R = random.randint(5, 15)
        start_rad = random.randint(0, 90)
        for n in range(0, 5):
            x = R * math.cos(math.radians(start_rad + n * 72))
            y = R * math.sin(math.radians(start_rad + n * 72))
            pentagon.append(Point(x, y))
        self.coordinates = pentagon

    def draw(self):
        for i, p in enumerate(self.coordinates):
            plt.scatter(p.x, p.y, s=35)
            if i == len(self.coordinates) - 1:
                plt.plot([self.coordinates[i].x, self.coordinates[0].x], [self.coordinates[i].y, self.coordinates[0].y], 'k-', lw=2)
            else:
                plt.plot([self.coordinates[i].x, self.coordinates[i + 1].x], [self.coordinates[i].y, self.coordinates[i + 1].y], 'k-', lw=2)

        plt.title("Square Numbers", fontsize=19)
        plt.xlabel("Number", fontsize=10)
        plt.ylabel("Square of Number", fontsize=10)
        plt.tick_params(axis='both', which='major', labelsize=9)
        plt.axis('equal')
        plt.show()


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def select_item(n_item) -> int:
        while True:
            try:
                item = (input(f"Введите комманду (число 1-{n_item}): "))
                if 0 < int(item) <= n_item+1:
                    return int(item)
                else:
                    print("Неправильное число")
            except ValueError:
                print("Ошибка при вводе числа")

    @staticmethod
    def select():
        print(30 * "-", "МЕНЮ", 30 * "-")
        print("1. Добавить")
        print("2. Сгенерировать")
        print("3. Удалить")
        print("4. Определить пересекаются ли объекты")
        print("5. Сравнить площади объектов")
        print("6. Передвинуть объект")
        print("7. Нарисовать объект")
        print("8. Выход")
        print(73 * "-")
        item = Menu.select_item(8) - 1
        return Factory.JobMode[item]


def main() -> None:
    factory = Factory()

    job_mode = Menu.select()
    while job_mode != 'Exit':
        if job_mode == 'AddObj':
            factory.add_object()
        elif job_mode == 'GenObj':
            factory.gen_object()
        elif job_mode == 'DelObj':
            factory.del_object()
        elif job_mode == 'IsIntersect':
            factory.is_intersect()
        elif job_mode == 'MoveObj':
            factory.move()
        elif job_mode == 'Compare':
            factory.compare()
        elif job_mode == 'DrawObj':
            factory.draw()
        job_mode = Menu.select()


if __name__ == '__main__':
    main()
