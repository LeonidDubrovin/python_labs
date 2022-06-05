# лаб 2, лист 1, задание 10
# https://docs.google.com/document/d/1YFBrTEv7AVoGGMytxwdmFqqZgyAT5m7dPUXhzBnM8NA/edit

def get_numbers() -> list:
    nums = []
    while True:
        try:
            n = float(input("Введите число: "))
            nums.append(n)
            if len(nums) > 1:
                if nums[-1] >= nums[-2]:
                    break
        except ValueError:
            print("Это не число")
    return nums


def main():
    nums = get_numbers()
    print("Введённые чила: ", nums)


if __name__ == '__main__':
    main()
