import requests
from lesson_3.ex_14.lib.base_case import BaseCase
from lesson_3.ex_14.lib.assertions import Assertions
import allure


@allure.epic("Cases for DELETE method")
class TestUserDelete(BaseCase):

    @allure.description("This test checks DELETE method for unauthorized user")
    def test_user_delete(self):
        response = requests.post("https://playground.learnqa.ru/api/user/login",
                                 data={'email': 'vinkotov@example.com', 'password': '1234'})
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')

        response1 = requests.delete(
            "https://playground.learnqa.ru/api/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response1, 400)
        assert response1.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

    @allure.description("This test checks DELETE user DATA for authorized user")
    def test_get_deleted_user_data(self):
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        user_id = self.get_json_value(response1, "id")

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=register_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        response3 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response3, 200)

        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}")
        Assertions.assert_code_status(response4, 404)
