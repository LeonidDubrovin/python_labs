from math import sqrt

JobMode = ['AddObj', 'DelObj', 'WorkWithObj', 'Exit']

# todo  to Factory
tObjects = []


class Factory:
    @staticmethod
    def add_object():
        print("1. Quadrate")
        print("2. Pentagon")
        print("3. Triangle")
        print("4. Rectangle")
        item = Menu.select_item(4)

        new_obj = None
        if item == 0:
            new_obj = Quadrate()
        elif item == 1:
            new_obj = Pentagon()
        elif item == 2:
            new_obj = Triangle()
        elif item == 3:
            new_obj = Rectangle()
        tObjects.append(new_obj)

    @staticmethod
    def del_object():
        if len(tObjects):
            print("Какой объект удалить?")
            for i, obj in enumerate(tObjects):
                print("{})".format(i+1))
            item = Menu.select_item(len(tObjects))
            del tObjects[item]
        else:
            print("Нет элементов")

    @staticmethod
    def work_with_object():
        for i, obj in enumerate(tObjects):
            print(f"{i}) ")


class Figure:
    coordinates = []

    def get_coord(self):
        return self.coordinates

    def move(self):
        pass

    # todo to Factory
    def compare(self):
        pass

    # todo to Factory
    def is_intersect(self, T1, T2):
        pass


class Quadrate(Figure):
    num_coord = 4

    def __init__(self):
        print("Введите координаты квадрата")
        # var1, var2 = input("1) ").split()
        # self.coordinates.append([(float(var1), float(var2))])
        # var1, var2 = input("2) ").split()
        # self.coordinates.append([(float(var1), float(var2))])
        # var1, var2 = input("3) ").split()
        # var1, var2 = [float(var1), float(var2)]
        # if sqrt((self.coordinates[0][0] - var1) ** 2 + (self.coordinates[0][1] - var2) ** 2) <= \
        #     sqrt((self.coordinates[1][0] - var1) ** 2 + (self.coordinates[1][1] - var2) ** 2):
        i = 0
        while i < self.num_coord:
            try:
                var1, var2 = input(f"{i}) ").split()
                self.coordinates.append([(float(var1), float(var2))])
                i += 1
            except ValueError:
                print("Ошибка при вводе")


class Pentagon(Figure):
    num_coord = 5

    def __init__(self):
        super().__init__()


class Triangle(Figure):
    num_coord = 3

    def __init__(self):
        super().__init__()


class Rectangle(Figure):
    num_coord = 4

    def __init__(self):
        super().__init__()


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def select_item(n_item) -> int:
        while True:
            try:
                item = (input(f"Введите комманду (число 1-{n_item}): "))
                if 0 < int(item) <= n_item+1:
                    return int(item) - 1
                else:
                    print("Неправильное число")
            except ValueError:
                print("Ошибка при вводе числа")

    @staticmethod
    def select():
        print(30 * "-", "МЕНЮ", 30 * "-")
        print("1. Добавить")
        print("2. Удалить")
        print("3. Работать")
        print("4. Выход ")
        print(73 * "-")
        item = Menu.select_item(3)
        return JobMode[item]


def main() -> None:
    factory = Factory()

    job_mode = Menu.select()
    while job_mode != 'Exit':
        if job_mode == 'AddObj':
            factory.add_object()
        elif job_mode == 'DelObj':
            factory.del_object()
        elif job_mode == 'WorkWithObj':
            factory.work_with_object()
        job_mode = Menu.select()


if __name__ == '__main__':
    main()
