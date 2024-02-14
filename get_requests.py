import requests

web = 'https://net-school.cap.ru/'
result = requests.get(web)
# data = result.json()
print(result)
print('Код от сервера:', result.status_code)
# print(result.text)