from main import BooksCollector


# Тестовые данные вынесены отдельно
TEST_BOOKS = {
    'book_1': 'Гордость и предубеждение и зомби',
    'book_2': 'Что делать, если ваш кот хочет вас убить',
    'book_3': 'Война и мир',
    'book_4': 'Мастер и Маргарита',
    'book_5': 'Дюна',
    'book_6': 'Ревизор',
    'book_7': 'Двенадцать стульев',
    'book_8': 'Преступление и наказание',
    'book_9': 'Теремок',
    'book_10': 'Дракула',
    'book_11': 'Шерлок Холмс',
    'book_12': 'Маленький принц',
    'book_13': 'Гарри Поттер',
    'book_14': 'Книга_1',
    'book_15': 'Книга_2',
    'book_16': 'Книга_3',
}

TEST_GENRES = {
    'fantasy': 'Фантастика',
    'comedy': 'Комедии',
    'detective': 'Детективы',
    'horror': 'Ужасы',
    'fairy_tales': 'Сказки',
}


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_1'])
        collector.add_new_book(TEST_BOOKS['book_2'])
        assert len(collector.get_books_genre()) == 2

    # добавление одной книги и проверка, что у нее нет жанра
    def test_add_new_book_add_one_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_3'])
        assert collector.get_book_genre(TEST_BOOKS['book_3']) == ''

    # тесты на граничные значения имени книги:
    
    # добавление книги с названием длиной 0 символов
    def test_add_new_book_name_length_zero(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # добавление книги с названием длиной 40 символов  
    def test_add_new_book_name_length_max(self):
        collector = BooksCollector()
        max_length_name = 'A' * 40
        collector.add_new_book(max_length_name)
        assert max_length_name in collector.get_books_genre()

   # добавление книги с названием длиной 41 символ 
    def test_add_new_book_name_length_exceeded(self):
        collector = BooksCollector()
        too_long_name = 'A' * 41
        collector.add_new_book(too_long_name)
        assert too_long_name not in collector.get_books_genre()

   # добавление книги валидной длины (от 1 до 40 символов)
    def test_add_new_book_name_length_normal(self):
        collector = BooksCollector()
        valid_name = 'Книга'
        collector.add_new_book(valid_name)
        assert valid_name in collector.get_books_genre()

    # нельзя добавить одну книгу дважды
    def test_add_new_book_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_4'])
        collector.add_new_book(TEST_BOOKS['book_4'])
        assert len(collector.get_books_genre()) == 1

    # установка правильного жанра для существующей книги
    def test_set_book_genre_set_fantasy_genre(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_5'])
        collector.set_book_genre(TEST_BOOKS['book_5'], TEST_GENRES['fantasy'])
        assert collector.get_book_genre(TEST_BOOKS['book_5']) == TEST_GENRES['fantasy']

    # нельзя установить жанр несуществующей книги
    def test_set_book_genre_set_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', TEST_GENRES['fantasy'])
        assert 'Несуществующая книга' not in collector.get_books_genre()

    # получение книг определенного жанра
    def test_get_books_with_specific_genre_get_comedy_books(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_6'])
        collector.add_new_book(TEST_BOOKS['book_7'])
        collector.add_new_book(TEST_BOOKS['book_8'])
        
        collector.set_book_genre(TEST_BOOKS['book_6'], TEST_GENRES['comedy'])
        collector.set_book_genre(TEST_BOOKS['book_7'], TEST_GENRES['comedy'])
        collector.set_book_genre(TEST_BOOKS['book_8'], TEST_GENRES['detective'])
        
        comedy_books = collector.get_books_with_specific_genre(TEST_GENRES['comedy'])
        assert len(comedy_books) == 2
        assert TEST_BOOKS['book_6'] in comedy_books
        assert TEST_BOOKS['book_7'] in comedy_books

    # книги для детей не содержат жанры с возрастным рейтингом
    def test_get_books_for_children_filter_age_rating_books(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_9'])
        collector.add_new_book(TEST_BOOKS['book_10'])
        collector.add_new_book(TEST_BOOKS['book_11'])
        
        collector.set_book_genre(TEST_BOOKS['book_9'], TEST_GENRES['fairy_tales'])  # Без рейтинга
        collector.set_book_genre(TEST_BOOKS['book_10'], TEST_GENRES['horror'])  # С рейтингом
        collector.set_book_genre(TEST_BOOKS['book_11'], TEST_GENRES['detective'])  # С рейтингом
        
        children_books = collector.get_books_for_children()
        assert len(children_books) == 1
        assert TEST_BOOKS['book_9'] in children_books
        assert TEST_BOOKS['book_10'] not in children_books
        assert TEST_BOOKS['book_11'] not in children_books

    # добавление книги в избранное
    def test_add_book_in_favorites_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_12'])
        collector.add_book_in_favorites(TEST_BOOKS['book_12'])
        assert TEST_BOOKS['book_12'] in collector.get_list_of_favorites_books()

    # нельзя добавить в избранное книгу, которой нет в коллекции
    def test_add_book_in_favorites_add_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Недобавленная книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    # удаление книги из избранного
    def test_delete_book_from_favorites_remove_book(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_13'])
        collector.add_book_in_favorites(TEST_BOOKS['book_13'])
        collector.delete_book_from_favorites(TEST_BOOKS['book_13'])
        assert TEST_BOOKS['book_13'] not in collector.get_list_of_favorites_books()

    # получение списка избранных книг для нескольких книг
    def test_get_list_of_favorites_books_get_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book(TEST_BOOKS['book_14'])
        collector.add_new_book(TEST_BOOKS['book_15'])
        collector.add_new_book(TEST_BOOKS['book_16'])
        
        collector.add_book_in_favorites(TEST_BOOKS['book_14'])
        collector.add_book_in_favorites(TEST_BOOKS['book_16'])
        
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert TEST_BOOKS['book_14'] in favorites
        assert TEST_BOOKS['book_15'] not in favorites
        assert TEST_BOOKS['book_16'] in favorites
