import requests
import json
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


email = input('Введите email: ')
username = input('Введите имя пользователя: ')
date_of_birth = input('Введите дату рождения в формате YYYY-mm-dd: ')
password = ''.join(random.choice(string.ascii_letters) for i in range(15))


def register(email, date_of_birth, username, password):
    s = requests.Session()
    payload = {
        "date_of_birth": date_of_birth,
        "email": email,
        "password": password,
        "username": username,
    }
    create_user = s.post('https://discord.com/api/v9/auth/register', json=payload)
    captchaID = s.get('http://2captcha.com/in.php?key=6d2047f498b2f9d6dd6d823a876411dd&method=hcaptcha&sitekey=4c672d35-0701-42b2-88c3-78380b0db560&pageurl=https://discord.com/register/')
    a = json.loads(captchaID.content[3:])
    time.sleep(15)
    captcha_result = s.get(f'http://2captcha.com/res.php?key=6d2047f498b2f9d6dd6d823a876411dd&action=get&id={a}')

    browser = webdriver.Chrome()
    browser.get('https://discord.com/api/v9/auth/register/')
    assert "Python" in browser.title
    browser.execute_script(
        'document.querySelector("name["h-captcha-response"]").innerHTML = ' + "'" + json.loads(captcha_result.content[3:]) + "'"
    )
    browser.find_element(By.CSS_SELECTOR, "#checkbox")
    return create_user.content


def login(email, password):
    s = requests.Session()
    payload = {
        "login": email,
        "password": password
    }
    response = s.post('https://discord.com/api/v9/auth/login', json=payload)
    print(json.loads(response.content)['token'])
    return response.content


register_account = register(email, date_of_birth, username, password)

login_account = login(email, password)
