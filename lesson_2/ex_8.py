import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"


def test_task_tokens():
    response = requests.get(url)
    data = response.json()
    token, seconds = data.get("token"), data.get("seconds")

    while data.get("status") == "Job is NOT ready":
        time.sleep(2)
        data = requests.get(url, params={"token": token}).json()

    time.sleep(seconds)
    data = requests.get(url, params={"token": token}).json()
    status, result = data.get("status"), data.get("result")

    print(f"Задача завершена. Результат: {result}" if status == "Job is ready" else "Произошла ошибка при выполнении задачи.")
