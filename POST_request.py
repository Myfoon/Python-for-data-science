import json
import requests


my_personal_dict = {"name":"Viacheslav","surname":"Ivanov","contact":[{"email":"dummy.mail@gmail.com"},{"tg":None}]}




print(json.dumps(my_personal_dict))


print(type(json.dumps(my_personal_dict)))

response = requests.post("https://bot-besample.app/webhook/ed0c4fe4-ea61-4402-b50f-95db8602f97c",
                         json = my_personal_dict,
                         headers = {"Authorization": "8BrOGc5DXA8e3N5F11Efqxd5b8Fc3Hpz"})

print(response.text)
