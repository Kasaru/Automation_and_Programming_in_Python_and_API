import requests


class NewLocation:
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com/"  # Базовая ссылка
        key = "?key=qaclick123"  # Параметр для всех запросов
        post_resource = "/maps/api/place/add/json"  # Ресурс метода post
        post_url = f"{base_url}{post_resource}{key}"
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
        print(place_id)

        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        status_code = result_get.status_code
        print(f"Статус код: {status_code}")
        assert 200 == status_code, "Request failed"
        print("Проверка создания локации успешна")

        """Изменение созданной локации"""

        put_resource = "/maps/api/place/update/json"
        put_url = f"{base_url}{put_resource}{key}"
        print(put_url)
        json_for_update_new_location = {

            "place_id": f"{place_id}",

            "address": "100 Lenina street, RU",

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
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
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
        assert check_address_info == "100 Lenina street, RU", "Обновление локации не удалось"

        """Удаление созданной локации"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = f"{base_url}{delete_resource}{key}"
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": f"{place_id}"
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        status_code = result_get.status_code
        print(f"Статус код: {status_code}")
        assert 200 == status_code, "Request failed"
        print("Проверка удаления локации успешна")
        check_delete = result_delete.json()
        check_delete_info = check_delete.get("status")
        print(f"Ответ: {check_delete_info}")
        assert check_delete_info == "OK", "Обновление локации не удалось"

        """Проверка удаления новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
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

        print(f"Тестирование TestNewLocation завершено успешно!")


new_place = NewLocation()
new_place.test_create_new_location()
