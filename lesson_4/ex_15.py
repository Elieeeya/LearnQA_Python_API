import allure
import requests
import pytest
from lesson_3.ex_14.lib.base_case import BaseCase
from lesson_3.ex_14.lib.assertions import Assertions
from datetime import datetime

@allure.epic("User registration cases")
class TestUserRegister(BaseCase):
    url = 'https://playground.learnqa.ru/api/user/'

    def generate_email(self):
        return f"test{datetime.now().strftime('%m%d%Y%H%M%S')}@example.com"

    # Тест на создание пользователя с некорректным email - без символа @
    def test_create_user_with_wrong_email(self):
        invalid_email = self.generate_email().replace('@', '')
        data = {'password': '1234', 'username': 'test', 'firstName': 'test', 'lastName': 'test', 'email': invalid_email}
        response = requests.post(self.url, data=data)
        Assertions.assert_code_status(response, 400)

    # Тест на создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить,
    # что отсутствие любого параметра не дает зарегистрировать пользователя
    @pytest.mark.parametrize('missing_field', ['password', 'username', 'firstName', 'lastName', 'email'])
    def test_create_user_with_missing_field(self, missing_field):
        data = {'password': '1234', 'username': 'test', 'firstName': 'test', 'lastName': 'test',
                'email': self.generate_email()}
        del data[missing_field]
        response = requests.post(self.url, data=data)
        Assertions.assert_code_status(response, 400)

    # Тест на создание пользователя с очень коротким именем в один символ
    def test_create_user_with_short_name(self):
        unique_email = self.generate_email()
        data = {'password': '1234', 'username': 't', 'firstName': 'test', 'lastName': 'test', 'email': unique_email}
        response = requests.post(self.url, data=data)
        Assertions.assert_code_status(response, 400)

    # Тест на создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_with_long_name(self):
        unique_email = self.generate_email()
        long_name = "a" * 251
        data = {'password': '1234', 'username': long_name, 'firstName': 'test', 'lastName': 'test',
                'email': unique_email}
        response = requests.post(self.url, data=data)
        Assertions.assert_code_status(response, 400)
