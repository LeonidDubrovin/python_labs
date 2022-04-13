import operator


class Book:
    def __init__(self, name: str, authors: list, date: str, publisher: str):
        self.name = name
        self.date = date
        self.publisher = publisher
        self.authors = []
        for a in authors:
            self.authors.append(a)

    def __str__(self) -> str:
        string = ''
        for a in self.authors:
            string += f"{a}, "
        string += f"{self.date}, "
        string += f"\"{self.name}\", "
        string += f"{self.publisher}"
        return string


class HomeLibrary:
    def __init__(self):
        self.lib = []

    # def __find(self, book: Book):
    #     b = self.search(book.name, op='name')
    #     if b:
    #         return b

    def add_book(self, book: Book):
        self.lib.append(book)

    # def delete_book(self, name):
    #     books = self.search(name, 'name')
    #     # for b in books:

    def delete_book(self, book: Book):
        self.lib.remove(book)

    def _search_by_name(self, b: Book, request: str):
        if b.name.find(request) != -1:
            return b

    def _search_by_publisher(self, b: Book, request: str):
        if b.publisher.find(request) != -1:
            return b

    def _search_by_date(self, b: Book, request: str):
        if b.date.find(request) != -1:
            return b

    def _search_by_authors(self, b: Book, request: str):
        for a in b.authors:
            if a.find(request) != -1:
                return b

    def search(self, request: str, op=None) -> list:
        books = []
        try:
            for b in self.lib:
                if op is not None:
                    if op == 'name':
                        if self._search_by_name(b, request):
                            books.append(b)
                            continue
                    elif op == 'publisher':
                        if self._search_by_publisher(b, request):
                            books.append(b)
                            continue
                    elif op == 'date':
                        if self._search_by_date(b, request):
                            books.append(b)
                            continue
                    elif op == 'authors':
                        if self._search_by_authors(b, request):
                            books.append(b)
                            continue
                else:
                    if self._search_by_name(b, request):
                        books.append(b)
                        continue
                    if self._search_by_publisher(b, request):
                        books.append(b)
                        continue
                    if self._search_by_date(b, request):
                        books.append(b)
                        continue
                    if self._search_by_authors(b, request):
                        books.append(b)
                        continue
            return books
        except ValueError:
            print("Ошибка при поиске")

    def sort_by(self, op):
        self.lib = sorted(self.lib, key=operator.attrgetter(op))

    def get_books(self) -> list:
        return self.lib


def get_menu_choice(lb: HomeLibrary):
    def print_menu():
        print(30 * "-", "МЕНЮ", 30 * "-")
        print("1. Вывести список книг ")
        print("2. Поиск книги по запросу ")
        print("3. Добавить книгу ")
        print("4. Удалить книгу ")
        print("5. Сортировать")
        print("6. Выход ")
        print(73 * "-")

    def print_sort_menu():
        print(30 * "-", "СОРТИРОВКА", 30 * "-")
        print("1. По названию ")
        print("2. По дате ")
        print("3. По издательству ")
        print("4. Выход ")
        print(73 * "-")

    loop = True

    print_menu()
    while loop:
        choice = input("Ввдеите комманду (число 1-6): ")

        if choice == '1':
            for i, b in enumerate(lb.get_books()):
                print(f"{i+1}) {b}")
        elif choice == '2':
            req = input("Введите запрос для поиска книги: ")
            books = lb.search(req)
            print("Найденные книги:")
            for b in books:
                print(b)
        elif choice == '3':
            name = input("Название книги: ")
            date = input("Дата первой публикации: ")
            publisher = input("Издательство: ")
            authors = []
            for a in input("Авторы (через запятую): ").split(","):
                authors.append(a.strip())
            lb.add_book(
                Book(name=name,
                     authors=authors,
                     date=date,
                     publisher=publisher))
        elif choice == '4':
            name = input("Ввдеите название книги для удаления: ")
            books = lb.search(name, op='name')
            if books:
                print("Найденные книги")
                for i, b in enumerate(books):
                    print(f"{i+1}) {b}")
                index_del = int(input("Книгу с каким номером удалить?: "))
                if index_del:
                    lb.delete_book(books[index_del - 1])
                    print("Книга удалена")
                else:
                    print("Неверно введен номер")
            else:
                print("Книги не найдены")

        elif choice == '5':
            print_sort_menu()
            str_choice = input("Ввдеите число [1-3]: ")
            if str_choice == '1':
                lb.sort_by('name')
            elif str_choice == '2':
                lb.sort_by('date')
            elif str_choice == '3':
                lb.sort_by('publisher')
            else:
                input("Неправильный выбор меню. Нажмите любую клавишу, чтобы повторить попытку..")
        elif choice == '6':
            print("Выход..")
            loop = False
        else:
            input("Неправильный выбор меню. Нажмите любую клавишу, чтобы повторить попытку..")


def main() -> None:
    lb = HomeLibrary()

    lb.add_book(
        Book(name="История России в датах",
             authors=["Орлов Александр Сергеевич", "Георгиев Владимир Анатольевич"],
             date="2021",
             publisher="РГ-Пресс"))
    lb.add_book(
        Book(name="География 10-11 классы. Контурные карты к учебнику В.П. Максаковского",
             authors=["А.Е. Козаренко"],
             date="2021",
             publisher="Просвещение"))
    lb.add_book(
        Book(name="Мастер и Маргарита",
             authors=["Булгаков Михаил Афанасьевич"],
             date="1967 ",
             publisher=""))

    get_menu_choice(lb)


if __name__ == '__main__':
    main()
