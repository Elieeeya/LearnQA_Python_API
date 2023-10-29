import allure
import requests
from lesson_3.ex_14.lib.base_case import BaseCase
from lesson_3.ex_14.lib.assertions import Assertions


@allure.epic("Cases for GET method")
class TestUserGet(BaseCase):
    @allure.description("Negative test: user is not authorized")
    def test_get_user_details_not_auth(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")
        Assertions.assert_json_has_key(response, "username")
        for field in ["email", "firstName", "lastName"]:
            Assertions.assert_json_has_not_key(response, field)

    def test_get_user_details_auth_as_same_user(self):
        auth_data = {"email": "vinkotov@example.com", "password": "1234"}
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")
        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})
        Assertions.assert_json_has_keys(response2, ["username", "email", "firstName", "lastName"])
