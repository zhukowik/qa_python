from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        book.set_book_genre('Кот', 'Ужасы')
        assert book.get_books_genre() == {'Кот' : 'Ужасы'}

    def test_get_book_genre(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        book.set_book_genre('Кот', 'Ужасы')
        assert book.get_book_genre('Кот') == 'Ужасы'

    def test_books_with_specific_genre(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        book.add_new_book('Собака')
        book.set_book_genre('Собака', 'Ужасы')
        book.set_book_genre('Кот', 'Ужасы')
        assert book.get_books_with_specific_genre('Ужасы') == ['Кот', 'Собака']

    def test_get_books_genre(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        assert book.get_books_genre() == {'Кот' : ''}

    def test_get_books_for_children(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        book.add_new_book('Собака')
        book.add_new_book('Рыбка')
        book.set_book_genre('Собака', 'Мультфильмы')
        book.set_book_genre('Кот', 'Комедии')
        book.set_book_genre('Рыбка', 'Фантастика')
        assert book.get_books_for_children() == ['Кот', 'Собака', 'Рыбка']

    def test_get_books_for_children_books_with_an_age_rating_are_not_included_in_the_list(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        book.set_book_genre('Кот', 'Ужасы')
        book.add_new_book('Собака')
        book.set_book_genre('Собака', 'Мультфильмы')
        assert book.get_books_for_children() == ['Собака']

    def test_add_book_in_favorites_add_two_books(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        book.add_new_book('Собака')
        book.add_book_in_favorites('Кот')
        book.add_book_in_favorites('Собака')
        assert  'Кот', 'Собака' in book.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        book.add_new_book('Собака')
        book.add_book_in_favorites('Кот')
        book.add_book_in_favorites('Собака')
        book.delete_book_from_favorites('Кот')
        assert not 'Кот' in book.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        book = BooksCollector()
        book.add_new_book('Кот')
        book.add_book_in_favorites('Кот')
        assert  'Кот' in book.get_list_of_favorites_books()