# лаб 2, лист 2, задание 13
# https://docs.google.com/document/d/1YFBrTEv7AVoGGMytxwdmFqqZgyAT5m7dPUXhzBnM8NA/edit

def get_ab():
    while True:
        try:
            a, b = [int(float(x)) for x in input("Введите числа a и b: ").split()]
            if a > b:
                print("a не может быть больше b")
            else:
                break
        except ValueError:
            print("Введите два числа через пробел")

    return a, b


def find_product(a, b) -> list:
    arr = []
    for x in range(a, b+1):
        for y in range(x, b+1):
            arr.append((x, y, x*y))
    return arr


def main():
    a, b = get_ab()
    print('a = {}, b = {}'.format(a, b))
    arr = find_product(a, b)
    for item in arr:
        print('{}*{} = {}'.format(item[0], item[1], item[2]))


if __name__ == '__main__':
    main()
