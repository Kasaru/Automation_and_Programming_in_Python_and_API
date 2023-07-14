import requests


class TestNewLocation:
    """Работа с новой локацией"""
    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com/"  # Базовая ссылка
        self.key = "?key=qaclick123"  # Параметр для всех запросов

    def file_writer(self,place_id):
        file = open("place_id.txt", "a")
        file.write(place_id + "\n")
        file.close()
    def file_reader(self,i):
        file = open("place_id.txt", "r")
        place_id = file.readlines()
        file.close()
        return place_id[i].replace("\n","")

    def file_cleaner(self):
        file = open("place_id.txt", "w")
        file.write("")
        file.close()

    def post_request_create_new_location(self):
        post_resource = "/maps/api/place/add/json"  # Ресурс метода post
        post_url = f"{self.base_url}{post_resource}{self.key}"
        print(post_url)
        json_for_create_new_location = {
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
        assert 200 == status_code, "Request failed"
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f"Статус код ответа: {check_info_post}")
        assert check_info_post == "OK", "Request failed"
        place_id = check_post.get("place_id")
        print(f"Place ID: {place_id}")
        new_place.file_writer(place_id)

    def get_request_for_new_location(self,i):
        place_id = new_place.file_reader(i)
        get_resource = "/maps/api/place/get/json"
        get_url = f"{self.base_url}{get_resource}{self.key}&place_id={place_id}"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        status_code = result_get.status_code
        print(f"Статус код: {status_code}")
        assert 200 == status_code, "Request failed"
        print("Проверка создания локации успешна")

    def put_request_for_new_location(self,i):
        """Изменение созданной локации"""
        place_id = new_place.file_reader(i)
        put_resource = "/maps/api/place/update/json"
        put_url = f"{self.base_url}{put_resource}{self.key}"
        print(put_url)
        json_for_update_new_location = {

            "place_id": f"{place_id}",

            "address": "Kremlin",

            "key": "qaclick123"

        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        status_code = result_put.status_code
        print(f"Статус код: {status_code}")
        assert 200 == status_code, "Request failed"
        print("Проверка изменения локации успешна")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print(f"Сообщение: {check_put_info}")
        assert check_put_info == "Address successfully updated", "Обновление локации не удалось"

        """Проверка изменения новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = f"{self.base_url}{get_resource}{self.key}&place_id={place_id}"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        status_code = result_get.status_code
        print(f"Статус код: {status_code}")
        assert 200 == status_code, "Request failed"
        print("Проверка изменения локации успешна")
        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print(f"Адрес: {check_address_info}")
        assert check_address_info == "Kremlin", "Обновление локации не удалось"

    def delete_request_for_new_location(self, i):
        """Удаление созданной локации"""
        place_id = new_place.file_reader(i)
        delete_resource = "/maps/api/place/delete/json"
        delete_url = f"{self.base_url}{delete_resource}{self.key}"
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": f"{place_id}"
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        status_code = result_delete.status_code
        print(f"Статус код: {status_code}")
        assert 200 == status_code, "Request failed"
        print("Проверка запроса на удаление локации успешна")
        check_delete = result_delete.json()
        check_delete_info = check_delete.get("status")
        print(f"Ответ: {check_delete_info}")
        assert check_delete_info == "OK", "удаление локации не удалось"
        print("Проверка удаления локации успешна")

        """Проверка удаления новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = f"{self.base_url}{get_resource}{self.key}&place_id={place_id}"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        status_code = result_get.status_code
        print(f"Статус код: {status_code}")
        assert 404 == status_code, "Request failed"
        print("Проверка удаления локации успешна")
        check_message = result_get.json()
        check_message_info = check_message.get("msg")
        print(f"Сообщение: {check_message_info}")
        assert check_message_info == "Get operation failed, looks like place_id  doesn't exists", "Удаление локации " \
                                                                                                  "не удалось"
        print("Проверка сообщения при удалении локации успешна")
        print(f"Тестирование TestNewLocation локация {i+1} завершено успешно!")





new_place = TestNewLocation()
"""Создание новой локации"""
for i in range(5):
    new_place.post_request_create_new_location()
for i in range(5):
    new_place.get_request_for_new_location(i)
    new_place.put_request_for_new_location(i)
    new_place.delete_request_for_new_location(i)
new_place.file_cleaner()