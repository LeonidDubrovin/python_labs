# 4 глава вариант 4, стр.174
from operator import attrgetter


class AEROFLOT:
    def __init__(self, des, fn, at):
        self.destination = des
        self.flight_number = fn
        self.airplane_type = at

    def __str__(self):
        return 'destination={0}, flight_number={1}, airplane_type={2}'.format(
            self.destination, self.flight_number, self.airplane_type)


class DBase:
    def __init__(self):
        self.airplanes = []

    def __del__(self):
        del self.airplanes

    def add_airplane(self, ap: AEROFLOT):
        self.airplanes.append(ap)

    def show_destination(self, d: str) -> list:
        tmp_list = []
        for ap in self.airplanes:
            if d == ap.destination:
                tmp_list.append(ap)
        return tmp_list

    def sort_by_flight_number(self):
        self.airplanes.sort(key=attrgetter('flight_number'))


class Menu:
    @staticmethod
    def select_item(n_item) -> int:
        while True:
            try:
                item = (input(f"Ввдеите комманду (число 1-{n_item}): "))
                if 0 < int(item) <= n_item + 1:
                    return int(item)
                else:
                    print("Неправильное число")
            except ValueError:
                print("Ошибка при вводе числа")

    @staticmethod
    def select():
        menu_items = {
            1: 'Создать объекты',
            2: 'Сгенерировать объекты',
            3: 'Показать все рейсы',
            4: 'Показать рейс в место назначения',
            5: 'Выход'
        }
        print(30 * "-", "МЕНЮ", 30 * "-")
        for key in menu_items:
            print('{0}){1}'.format(key, menu_items[key]))
        print(66 * "-")
        item = Menu.select_item(len(menu_items))
        return item


def main() -> None:
    db = DBase()
    while True:
        choice = Menu.select()
        if choice == 1:
            for i in range(3):
                dest, fn, at = [str(i) for i in
                                input('Введите: (место назначения) (номер рейса) (тип самолета): ').split()]
                db.add_airplane(AEROFLOT(dest, fn, at))
            db.sort_by_flight_number()
            print("Рейсы введены")

        if choice == 2:
            db.add_airplane(AEROFLOT('Murmansk', 'S5689', 'Boeing 777'))
            db.add_airplane(AEROFLOT('Novosibirsk', 'AB1263', 'Boeing 747'))
            db.add_airplane(AEROFLOT('Moscow', 'VC3218', 'Boeing 777'))
            db.add_airplane(AEROFLOT('Moscow', 'F1197', 'Boeing 747'))
            db.add_airplane(AEROFLOT('Moscow', 'S9757', 'Boeing 777'))
            db.add_airplane(AEROFLOT('Tomsk', 'AB8921', 'Boeing 777'))
            db.add_airplane(AEROFLOT('Moscow', 'VC3217', 'Boeing 777'))
            db.sort_by_flight_number()
            print("Рейсы сгенерированы")

        elif choice == 3:
            aps = db.airplanes
            if len(aps) > 0:
                for ap in aps:
                    print(ap)
            else:
                print("Нет рейсов")

        elif choice == 4:
            d = str(input(f"Ввдеите место назначения: "))
            print("Рейсы в данное место назначения: {}".format(d))
            aps = db.show_destination(d)
            if len(aps) > 0:
                for ap in aps:
                    if d == ap.destination:
                        print(ap)
            else:
                print("Нет рейсов с таким местом назначения")

        elif choice == 5:
            print("Завершение работы программы")
            break
        else:
            print("Неправильная комманда")


if __name__ == '__main__':
    main()
