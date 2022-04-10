import re


class MyString:
    def __init__(self, string):
        self.string = string

    def __setattr__(self, attr, string):
        if attr == 'string':
            self.__dict__[attr] = string

    def __add__(self, string):
        # return str(self.string) + str(string.string)
        return self.string + str(string)

    def __str__(self):
        return self.string

    def __lt__(self, other):
        return self.string < other

    def __gt__(self, other):
        return self.string > other

    def to_digit(self) -> list:
        try:
            nums = re.findall(r"(?:\d+\.\d+|\d+)", self.string)
            return nums
        except ValueError:
            print("Возникла ошибка при выделении числа")

    def to_int(self) -> list:
        nums = self.to_digit()
        for i, num in enumerate(nums):
            nums[i] = int(float(num))
        return nums

    def to_float(self):
        nums = self.to_digit()
        for i, num in enumerate(nums):
            nums[i] = float(num)
        return nums

    def to_bool(self):
        nums = self.to_digit()
        ans = False
        for i, num in enumerate(nums):
            try:
                if float(num):
                    ans = True
            except ValueError:
                pass
        return ans


def get_menu_choice(strings: list):
    def print_menu():
        print(30 * "-", "МЕНЮ", 30 * "-")
        print("1. Вывести строки ")
        print("2. Добавить строку ")
        print("3. Извлечь число ")
        print("4. Преобразовать в число нужного типа")
        print("5. Стравнить строки ")
        print("6. Выход ")
        print(73 * "-")

    def print_type_menu():
        print(30 * "-", "ТИПЫ", 30 * "-")
        print("1. int ")
        print("2. float ")
        print("3. bool ")
        print("4. Выход ")
        print(73 * "-")
    loop = True

    print_menu()
    while loop:
        choice = input("Ввдеите комманду (число 1-5): ")

        if choice == '1':
            for i, s in enumerate(strings):
                print(f"{i+1}) {s}")
        elif choice == '2':
            try:
                s = MyString(input("Введите строку: "))
                strings.append(s)
            except ValueError:
                print("Возникла ошибка при добавлении строки")
        elif choice == '3':
            try:
                index = int(input("Введите номер нужной строки: "))
                if index < len(strings) + 1:
                    print(strings[index - 1].to_digit())
            except ValueError:
                print("Возникла ошибка при извлечении числа из строки")
        elif choice == '4':
            try:
                print_type_menu()
                type_choice = input("Ввдеите число [1-3]: ")
                if type_choice == '1':
                    for s in strings:
                        print(f"{s} to int = {s.to_int()}")
                elif type_choice == '2':
                    for s in strings:
                        print(f"{s} to float = {s.to_float()}")
                elif type_choice == '3':
                    for s in strings:
                        print(f"{s} to bool = {s.to_bool()}")
                else:
                    input("Неправильный выбор меню. Нажмите любую клавишу, чтобы повторить попытку..")
            except ValueError:
                print("Возникла ошибка при преобразовании типа")
        elif choice == '5':
            for i, s1 in enumerate(strings):
                for s2 in strings[:i]:
                    print("{} > {} ? : {}".format(s1, s2, s1 > s2))
                    print("{} < {} ? : {}".format(s1, s2, s1 < s2))
        elif choice == '6':
            print("Выход..")
            loop = False
        else:
            input("Неправильный выбор меню. Нажмите любую клавишу, чтобы повторить попытку..")


def main():
    # print(f'Hi, {name}')
    strings = []
    strings.append(MyString("16"))
    strings.append(MyString("65rwer"))
    strings.append(MyString("tttw12312rr"))
    strings.append(MyString("aa155.33pppp44.2aa"))
    strings.append(MyString("ergdsgdgf"))

    get_menu_choice(strings)


if __name__ == '__main__':
    main()
