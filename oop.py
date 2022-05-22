class A:
    def __init__(self):
        self.arr = ['A']


class B(A):
    num = 2

    def add(self, p):
        self.arr.append(p)


b1 = B()
b2 = B()
b1.add('B1')
b2.add('B2')
print(b1.arr)
print(b2.arr)

