import requests

url = 'https://playground.learnqa.ru/api/long_redirect'


# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
def test_request_of_any_type_without_parameters():
    response = requests.get(url)
    print(f"Текст ответа: {response.text}")


# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
def test_send_head():
    response = requests.head(url)
    print(response.status_code)
    print(response.text)


# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
def test_send_get():
    response = requests.get(url, params={'method': 'GET'})
    print(f"Текст ответа: {response.text}")


# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.

def test_all_method():
    methods = ['GET', 'POST', 'PUT', 'DELETE']

    for method in methods:
        for method_value in methods:
            if method == 'GET':
                response = requests.request(method, url, params={'method': method_value})
            else:
                response = requests.request(method, url, data={'method': method_value})
            print(f'Ответ на Ваш запрос {method}, с параметром {method_value}: {response.text}')
