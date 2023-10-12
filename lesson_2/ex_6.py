import requests

url = "https://playground.learnqa.ru/api/long_redirect"


def test_task_long_redirect():
    response = requests.get(url, allow_redirects=True)
    print(f"Количество редиректов: {len(response.history)}")
    print(f"Итоговый URL: {response.url}")
