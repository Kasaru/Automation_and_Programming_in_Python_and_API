import requests


class TestNewJoke():
    def __init__(self):
        pass
    def create_new_random_joke_test(self):
        url = "https://api.chucknorris.io/jokes/random"

        result = requests.get(url)
        result.encoding = "utf-8"
        print(result.text)
        assert 200 == result.status_code, "Url is incorrect"
        print(f"Status code: {result.status_code}")
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        print(check.get("value"))
        assert check_info == [], "incorrect category"
        assert "Chuck" in check.get("value"), "IT IS NOT CHUCK'S JOKE!!!!"

random_joke = TestNewJoke()
random_joke.create_new_random_joke_test()