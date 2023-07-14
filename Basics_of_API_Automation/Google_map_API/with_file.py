import requests


class TestNewLocation:
    """Работа с новой локацией"""
    def __init__(self):
        """Инициализация общих переменных"""

        self.base_url = "https://rahulshettyacademy.com/"  # Базовая ссылка
        self.key = "?key=qaclick123"  # Параметр для всех запросов

    def file_writer(self,place_id):

        """Запись в файл"""

        file = open("place_id.txt", "a")
        file.write(place_id + "\n")
        file.close()
    def file_reader(self,i):

        """Построчное считывание из файла"""

        file = open("place_id.txt", "r")
        place_id = file.readlines()
        file.close()
        return place_id[i].replace("\n","")

    def file_cleaner(self):

        """Очистка файла """

        file = open("place_id.txt", "w")
        file.write("")
        file.close()

    def post_request_create_new_location(self,i):
        """Создание новой локации"""

        post_resource = "/maps/api/place/add/json"  # Ресурс метода post
        post_url = f"{self.base_url}{post_resource}{self.key}" # составная ссылка метода post
        print(post_url)
        json_for_create_new_location = {    # Тело post запроса
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        status_code = result_post.status_code
        print(f"Статус код: {status_code}")
        assert 200 == status_code, "Post request failed"    # Проверка на успешный запрос (код)
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f"Статус код ответа: {check_info_post}")
        assert check_info_post == "OK", "Post request failed"   # Проверка на успешный запрос (текст)
        place_id = check_post.get("place_id")
        print(f"Place ID: {place_id}")
        new_place.file_writer(place_id)
        print(f"Количество созданных локаций: {i + 1}")

    def get_request_for_new_location(self,i):
        """Считывание данных созданной локации"""

        place_id = new_place.file_reader(i)
        get_resource = "/maps/api/place/get/json" # Ресурс метода get
        get_url = f"{self.base_url}{get_resource}{self.key}&place_id={place_id}" # составная ссылка метода get
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        status_code = result_get.status_code
        print(f"Статус код: {status_code}")
        assert 200 == status_code, "Get request failed" # # Проверка на успешный запрос (код)
        print("Проверка создания локации успешна")
        print(f"Количество проверенных локаций: {i+1}")

new_place = TestNewLocation()
for i in range(5):
    new_place.post_request_create_new_location(i) # вызов функции для создания локации
for i in range(5):
    new_place.get_request_for_new_location(i) # Вызов функции для проверки созданной локации
print("Тестирование создания новых локаций TestNewLocation завершено успешно!")
#new_place.file_cleaner() # Очистка файла с записанными place_id