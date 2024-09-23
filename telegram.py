import sys
import requests
# ACCOUNT = sys.argv[1]

TOKEN = "6815228522:AAFl1umxHLB0DCNSf0D3RDdiXPbUfr1Sc7E"
chat_id = "729044367"
message = "Задание успешно выполнено!"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())