import pytest
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

    @pytest.mark.parametrize('book_title,genre', [
        ('1984', 'Фантастика'),
        ('Книга 1', 'Комедии')
    ])
    def test_set_book_genre_two_books(self, book_title, genre):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        assert collector.get_book_genre(book_title) == genre

    def test_book_has_genre_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 3')
        assert collector.get_book_genre('Книга 3') == ''

    def test_get_books_with_specific_genre_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert 'Книга 1' in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_for_children_not_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга ужасов')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        assert 'Книга ужасов' not in collector.get_books_for_children()

    def test_get_books_for_children_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга сказок')
        collector.set_book_genre('Книга сказок', 'Мультфильмы')
        assert 'Книга сказок' in collector.get_books_for_children()

    def test_add_book_in_favorites_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_new_book_missing(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        assert 'Книга 1' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 2')
        collector.delete_book_from_favorites('Книга 2')
        assert 'Книга 2' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_clear_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.add_book_in_favorites('Книга 2')
        collector.add_book_in_favorites('Книга 3')
        collector.delete_book_from_favorites('Книга 2')
        assert 'Книга 3' in collector.get_list_of_favorites_books()