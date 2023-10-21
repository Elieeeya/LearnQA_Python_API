import requests

url = 'https://playground.learnqa.ru/api/homework_header'


def test_header_method_request():
    response = requests.get(url)

    for header, value in response.headers.items():
        print(header + ': ' + value)

    assert response.headers['x-secret-homework-header'] == 'Some secret value'
