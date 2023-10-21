import requests

url = 'https://playground.learnqa.ru/api/homework_cookie'


def test_cookie_method_request():
    response = requests.get(url)

    for cookie in response.cookies:
        print(f'Имя cookie {cookie.name}, Значение cookie {cookie.value}')

    assert response.cookies['HomeWork'] == 'hw_value'
