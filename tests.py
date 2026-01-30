from main import BooksCollector


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # добавление одной книги и проверка, что у нее нет жанра
    def test_add_new_book_add_one_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert collector.get_book_genre('Война и мир') == ''

    # нельзя добавить одну книгу дважды
    def test_add_new_book_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')  # Вторая попытка
        assert len(collector.get_books_genre()) == 1

    # установка правильного жанра для существующей книги
    def test_set_book_genre_set_fantasy_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # нельзя установить жанр несуществующей книги
    def test_set_book_genre_set_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    # получение книг определенного жанра
    def test_get_books_with_specific_genre_get_comedy_books(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_new_book('Двенадцать стульев')
        collector.add_new_book('Преступление и наказание')
        
        collector.set_book_genre('Ревизор', 'Комедии')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        
        comedy_books = collector.get_books_with_specific_genre('Комедии')
        assert len(comedy_books) == 2
        assert 'Ревизор' in comedy_books
        assert 'Двенадцать стульев' in comedy_books

    # книги для детей не содержат жанры с возрастным рейтингом
    def test_get_books_for_children_filter_age_rating_books(self):
        collector = BooksCollector()
        collector.add_new_book('Теремок')
        collector.add_new_book('Дракула')
        collector.add_new_book('Шерлок Холмс')
        
        collector.set_book_genre('Теремок', 'Cказка')  # Без рейтинга
        collector.set_book_genre('Дракула', 'Ужасы')  # С рейтингом
        collector.set_book_genre('Шерлок Холмс', 'Детективы')  # С рейтингом
        
        children_books = collector.get_books_for_children()
        assert len(children_books) == 1
        assert 'Теремок' in children_books
        assert 'Дракула' not in children_books

    # добавление книги в избранное
    def test_add_book_in_favorites_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        assert 'Маленький принц' in collector.get_list_of_favorites_books()

    # нельзя добавить в избранное книгу, которой нет в коллекции
    def test_add_book_in_favorites_add_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    # удаление книги из избранного
    def test_delete_book_from_favorites_remove_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    # получение списка избранных книг для нескольких книг
    def test_get_list_of_favorites_books_get_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_1')
        collector.add_new_book('Книга_2')
        collector.add_new_book('Книга_3')
        
        collector.add_book_in_favorites('Книга_1')
        collector.add_book_in_favorites('Книга_3')
        
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Книга_1' in favorites
        assert 'Книга_2' not in favorites
        assert 'Книга_3' in favorites
