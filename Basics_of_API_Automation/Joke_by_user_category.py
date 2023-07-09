import requests


class TestNewJoke:
    def __init__(self):
        pass

    def get_categories_list(self):
        """Получение списка категорий"""

        url = "https://api.chucknorris.io/jokes/categories"  # Ссылка на категории
        print(f"URL: {url}")  # Вывод ссылки
        result = requests.get(url)  # Запись ответа по гет запросу
        print(f"Categories status code: {result.status_code}\n")  # Вывод статус кода отправленного запроса
        assert 200 == result.status_code, f"Url is incorrect {url}"  # Проверка на успешный запрос
        result.encoding = "utf-8"  # Указание кодировки ответа
        categories = result.json()  # Запись списка категорий в переменную
        return categories  # Возврат списка категорий

    def create_new_joke_test(self):
        """Создание шутки по категории"""
        category = joke.request_category().lower()  # Запрос ввода категории шутки у пользователя
        categories_list = joke.get_categories_list()  # Создание списка категорий
        assert category in categories_list, f"categories_list doesn't contain category: {category}"
        print("Category number: " + str(categories_list.index(category) + 1))  # Вывод номера категории
        print(f"Category name: {category}\n")  # Вывод категории
        url = f"https://api.chucknorris.io/jokes/random?category={category}"  # Подстановка категории в адрес ссылки
        print(f"URL: {url}")  # Вывод ссылки
        result = requests.get(url)  # Запись ответа по гет запросу
        print(f"Status code: {result.status_code}")  # Вывод статус кода отправленного запроса
        assert 200 == result.status_code, f"Url is incorrect {url}"  # Проверка на успешный запрос
        result.encoding = "utf-8"  # Указание кодировки ответа
        new_joke = result.json()  # Запись ответа по запросу в переменную
        assert "Chuck" in new_joke.get(
            "value"), f"THIS IS NOT CHUCK'S JOKE!!!! {new_joke.get('value')}"  # Проверка на наличие Chuck в шутке
        print(f"Joke: {new_joke.get('value')}\n")  # Вывод шутки

    def request_category(self):
        """Запрос категории шутки у пользователя"""

        category = input("Введите категорию шутки: ")  # Ввод категории шутки пользователем
        return category  # Возврат введенной категории


joke = TestNewJoke()
joke.create_new_joke_test()
