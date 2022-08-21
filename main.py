import requests
import random
import string


api_key = "API_KEY"
discord_url = "https://discord.com/register/"
site_key = "4c672d35-0701-42b2-88c3-78380b0db560"
email = input('Введите email: ')
username = input('Введите имя пользователя: ')
date_of_birth = input('Введите дату рождения в формате YYYY-mm-dd: ')
password = ''.join(random.choice(string.ascii_letters) for i in range(15))


def register(email, date_of_birth, username, password):
    request_captchaID = requests.get(f'http://2captcha.com/in.php?key={api_key}&method=hcaptcha&sitekey={site_key}&pageurl={discord_url}')
    captchaID = request_captchaID.text
    captchaID = captchaID.replace("OK|", "")
    print("Идет обработка hCAPTCHA...")
    while True:
        request_captcha_token = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={captchaID}')
        captcha_token = request_captcha_token.text
        if "OK" in captcha_token:
            captcha_token = captcha_token.replace("OK|", "")
            payload = {
                "date_of_birth": date_of_birth,
                "email": email,
                "password": password,
                "username": username,
                "captcha_key": captcha_token
            }
            create_user = requests.post('https://discord.com/api/v9/auth/register', json=payload)
            print(create_user.content)
            exit()
            return create_user.content


register_account = register(email, date_of_birth, username, password)
