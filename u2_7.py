from math import sqrt
import re

# JobMode = ['AddObj', 'DelObj', 'WorkWithObj', 'Exit']

# todo  to Factory
# tObjects = []


class SymbString:
    def __init__(self, value=''):
        self.value = value

    def show(self):
        print('Текущее значение: ', self.value)

    def operator_inc(self, str):
        try:
            self.value = self.value + str.value
            print('Конкатенация строк: ', self.value)
        except ValueError:
            print("Ошибка при конкатенации строк")

    def __del__(self):
        print('Объект был уничтожен.')


class DecString(SymbString):
    def operator_inc(self, str):
        try:
            if type(self) == type(str):
                value1 = int(self.value)
                value2 = int(str.value)
                self.value = value1 + value2
            else:
                self.value += str.value
            print('Результат сложения: ', self.value)
        except ValueError:
            print("Ошибка при сложении десятичного числа и другого объекта")

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
    def delete(symbstr):
        del symbstr


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
                    if choice == 2:
                        x.show()

                    elif choice == 3:
                        y.show()

                    elif choice == 4:
                        x.operator_inc(y)

                    elif choice == 5:
                        y.operator_inc(x)

                    elif choice == 6:
                        x = factory.delete(x)
                        y = factory.delete(y)
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
