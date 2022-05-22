class A:
    arr = ['A']


class B(A):
    def __init__(self):
        pass

    def add(self, p):
        self.arr.append(p)


b1 = B()
b2 = B()
b1.add('B1')
b1.add('B2')
print(b1.arr)
print(b2.arr)

