from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, f"{error_message}. Expected value is {expected_value}, but actual value is {response_as_dict[name]}"

    @staticmethod
    def assert_json_has_key(response: Response, name):
        response_as_dict = response.json()
        assert name in response_as_dict, f"Response JSON doesn't have key {name}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        response_as_dict = response.json()
        assert name not in response_as_dict, f"Response JSON shouldn't have key {name}. But it's present."

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Unexpected status code! Expected: {expected_status_code}, Actual: {response.status_code}"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        response_as_dict = response.json()
        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key {name}"

    @staticmethod
    def assert_text_message(response: Response, status_code):
        assert status_code == 400, "Test didn't pass successfully"
