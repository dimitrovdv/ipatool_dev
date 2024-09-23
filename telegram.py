import sys
import requests
ACCOUNT = sys.argv[1]
bottoken = sys.argv[2]
chat_id = "729044367"
message = f"Задание успешно выполнено для аккаунта: {ACCOUNT}!"
url = f"https://api.telegram.org/bot{bottoken}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())