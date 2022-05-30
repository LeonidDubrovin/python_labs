from math import sqrt
import re

# были удалены принты из классов


class SymbString:
    def __init__(self, value=''):
        self.value = value

    def __add__(self, other):
        return SymbString(self.value + other.value)

    def __str__(self):
        return self.value


class DecString(SymbString):
    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if type(self) == type(other):
            value1 = int(self.value)
            value2 = int(other.value)
            value = value1 + value2
        else:
            value = self.value + other.value
        return DecString(value)


class Factory:
    @staticmethod
    def create_symb():
        value = str(input('Введите содержание строки: '))
        return SymbString(value)

    @staticmethod
    def create_dec():
        while True:
            dec_number = str(input('Введите десятичное число: '))
            if re.match(r'[0-9]+', dec_number) is not None:
                return DecString(dec_number)
            else:
                print(f'Неккоректный ввод десятичного числа. Попробуйте заново.\n')
                continue

    @staticmethod
    def delete(string):
        del string


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def select_item(n_item) -> int:
        while True:
            try:
                item = (input(f"Ввдеите комманду (число 1-{n_item}): "))
                if 0 < int(item) <= n_item+1:
                    return int(item)
                else:
                    print("Неправильное число")
            except ValueError:
                print("Ошибка при вводе числа")

    @staticmethod
    def select():
        menu_text = (
            '''
            1. Создать пару объектов
            2. Показать значение первого объекта
            3. Показать значение второго объекта
            4. Прибавить к первому второе значение
            5. Прибавить к второму первое значение
            6. Удалить объекты
            7. Выход'''
        )
        print(30 * "-", "МЕНЮ", 30 * "-")
        print(menu_text)
        print(73 * "-")
        item = Menu.select_item(7)
        return item


def main() -> None:
    factory = Factory()
    choice = Menu.select()
    while True:
        if choice == 1:
            print("Создать символьную строку: 1")
            print("Создать десятичную строку: 2")
            print("Первый объект:")
            type_str_input = Menu.select_item(2)
            if type_str_input == 1:
                x = factory.create_symb()
            elif type_str_input == 2:
                x = factory.create_dec()
            else:
                print('\nПеременная не была создана.')
                continue

            print("Второй объект:")
            type_str_input = Menu.select_item(2)
            if type_str_input == 1:
                y = factory.create_symb()
            elif type_str_input == 2:
                y = factory.create_dec()
            else:
                print('\nПеременная не была создана.')
                continue

            if x is not None and y is not None:
                while True:
                    choice = Menu.select()
                    if choice == 1:
                        print("Объекты уже созданы")
                        continue

                    if choice == 2:
                        print("Первый объект: ", x)

                    elif choice == 3:
                        print("Второй объект: ", y)

                    elif choice == 4:
                        x += y
                        print("Первый объект: ", x)

                    elif choice == 5:
                        y += x
                        print("Второй объект: ", y)

                    elif choice == 6:
                        factory.delete(x)
                        factory.delete(y)
                        break

                    elif choice == 7:
                        break

                    else:
                        print('Неккоректный ввод! Для начала необходимо создать пару объектов (операция 1)')
                        continue

        elif choice == 7:
            print("Завершение работы программы")
            break
        else:
            print("Создайте пару объектов")
            choice = Menu.select()


if __name__ == '__main__':
    main()
