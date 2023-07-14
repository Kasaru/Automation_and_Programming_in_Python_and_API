import requests


class TestDeleteNewLocation:
    """Работа с новой локацией"""

    def __init__(self):
        """Инициализация общих переменных"""

        self.base_url = "https://rahulshettyacademy.com/"  # Базовая ссылка
        self.key = "?key=qaclick123"  # Параметр для всех запросов
        self.cd = 0  # счетчик добавленных в файл локаций

    def file_writer(self, place_id, file_name):

        """Запись в файл"""

        file = open(f"{file_name}.txt", "a")  # Подстановка имени файла для записи
        file.write(place_id + "\n")
        file.close()

    def file_reader(self, i):

        """Построчное считывание из файла"""

        file = open("place_id.txt", "r")
        place_id = file.readlines()
        file.close()
        return place_id[i].replace("\n", "")

    def get_request_for_new_location(self, i):
        """Считывание данных созданной локации"""

        place_id = new_place.file_reader(i)
        get_resource = "/maps/api/place/get/json"  # Ресурс метода get
        get_url = f"{self.base_url}{get_resource}{self.key}&place_id={place_id}"  # составная ссылка метода get
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        status_code = result_get.status_code
        print(f"Статус код: {status_code}")
        if 404 == status_code:  # Проверка на успешный запрос (код)
            check_message = result_get.json()
            check_message_info = check_message.get("msg")
            print(f"Сообщение: {check_message_info}")
            assert check_message_info == "Get operation failed, looks like place_id  doesn't exists", "Удаление локации " \
                                                                                                      "не удалось"  # Проверка на успешное удаление(текст), локация отсутствует
            print("Проверка сообщения при удалении локации успешна")
            print(f"Проверка удаления локации {i + 1} place_id: {place_id} успешна")
            print(f"Количество проверенных локаций: {i + 1}\n")
        else:
            self.cd += 1
            new_place.file_writer(place_id, "wasnt_delete")  # Запись оставшихся локаций в новый файл
            print(f"Проверка создания локации {i + 1} успешна, локация добавлена в файл")
            print(f"Количество добавленных в файл локаций: {self.cd}")
            print(f"Количество проверенных локаций: {i + 1}\n")

    def delete_request_for_new_location(self, i):

        """Удаление созданной локации"""

        place_id = new_place.file_reader(i)
        delete_resource = "/maps/api/place/delete/json"  # Ресурс метода delete
        delete_url = f"{self.base_url}{delete_resource}{self.key}"  # Составная ссылка метода delete
        print(delete_url)
        json_for_delete_new_location = {  # Тело delete запроса
            "place_id": f"{place_id}"
        }
        if i == 1 or i == 3:
            result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
            print(f"Удалена локация {i + 1} place_id: {place_id}")
            status_code = result_delete.status_code
            print(f"Статус код: {status_code}")
            assert 200 == status_code, f"Request failed incorrect delete status code {status_code}"  # Проверка на успешное удаление(код)
            print("Проверка запроса на удаление локации успешна")
            check_delete = result_delete.json()
            check_delete_info = check_delete.get("status")
            print(f"Ответ: {check_delete_info}")
            assert check_delete_info == "OK", "удаление локации не удалось"  # Проверка на успешное удаление(текст)
            print("Проверка удаления локации успешна")
        else:
            print(f"Локация {i + 1} не подлежит удалению, place_id: {place_id}")
        print(f"Тестирование TestDeleteNewLocation локация {i + 1} завершено успешно!\n")


new_place = TestDeleteNewLocation()
for i in range(5):
    new_place.delete_request_for_new_location(i)  # Вызов функции для проверки удаления локации
for i in range(5):
    new_place.get_request_for_new_location(i)  # Вызов функции для проверки существования локации
print("Тестирование создания новых локаций TestDeleteNewLocation завершено успешно!")
