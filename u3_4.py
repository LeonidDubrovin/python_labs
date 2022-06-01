import ctypes


class VectError(Exception):
    def __init__(self, msg):
        if msg is None:
            msg = "An error occurred with Vect"
        super(VectError, self).__init__(msg)


class VectRangeError(VectError):
    def __init__(self, k, max_index):
        super(VectRangeError, self).__init__(msg=f"Vect Range Error: max index = {max_index}, your index = {k}")


class VectPopError(VectError):
    def __init__(self):
        super(VectPopError, self).__init__(msg="Vect Pop Error: Vect has no items")


class Vect:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.values = self._make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise VectRangeError(k, self.capacity - 1)
        return self.values[k]

    def append(self, element):
        if self.n == self.capacity:
            self._resize(1 + self.capacity)
        self.values[self.n] = element
        self.n += 1

    def pop(self):
        if self.capacity == 0:
            raise VectPopError()
        tmp = self.values[self.n - 1]
        self.n -= 1
        self._resize(self.capacity - 1)
        return tmp

    def _make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def _resize(self, new_cap):
        tmp_arr = self._make_array(new_cap)
        for k in range(self.n):
            tmp_arr[k] = self.values[k]
        self.values = tmp_arr
        self.capacity = new_cap


class Stack:
    def __init__(self):
        self.items = Vect()

    def push_back(self, item):
        self.items.append(item)

    def pop_back(self):
        self.items.pop()

    def size(self):
        return len(self.items)


def main() -> None:
    try:
        st = Stack()
        st.push_back(1)
        st.push_back(2)
        print(st.size())
        st.pop_back()
        st.pop_back()
        st.pop_back()
    except VectPopError as e:
        print(e)
    except VectRangeError as e:
        print(e)

    try:
        v = Vect()
        v.append(1)
        v.append(2)
        v.pop()
        v.pop()
        print(v[0])
    except VectPopError as e:
        print(e)
    except VectRangeError as e:
        print(e)


if __name__ == '__main__':
    main()
    # глава 3, задание 4
    # без шаблонов, только наследование
