import pytest

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] иниициализируем настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестововый класс")

@pytest.fixture(scope="function")
def user_client():
    print("[FUNCTION] Создаем API Клиент на каждый автотест")


class TestUerFlow:
    def test_user_can_login(self,settings,user,user_client):
        ...
    def test_user_can_create_course(self,settings,user,user_client):
        ...


class TestAccountFlow:
    def test_user_account(self,settings,user,user_client):
        ...

@pytest.fixture
def user_data():
    print("Создаем пользователя до теста(setup)")
    yield {"username": "test_user", "email": "test@example.com"}
    print("Удаляем пользователя после теста(teardown)")


def test_user_email(user_data:dict):
    print(user_data)
    assert user_data['email'] == 'test@example.com'

def test_user_username(user_data:dict):
    print(user_data)
    assert user_data['username'] == 'test_user'