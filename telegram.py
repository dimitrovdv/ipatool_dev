import requests
import os
from dotenv import load_dotenv
load_dotenv()
apple_id = os.getenv('apple_id')
bundle_id = os.getenv('bundle_id')
appid = os.getenv('appid')
print(apple_id)
print(bundle_id)
print(appid)

TOKEN = "8157033427:AAGKk7tsAAMCv_I87pVoLllZEuKlGJ8s0cQ"
chat_id = "729044367"
message = f"Задание для УЗ {apple_id} успешно выполнено! Куплено приложение: {bundle_id};{appid}!"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())