import pytest


@pytest.fixture()
def set_up():
    print("Вход в систему")
    yield
    print("\nВыход из системы")

@pytest.fixture(scope="function")
def some():
    print("Начало")
    yield
    print("\nКонец")