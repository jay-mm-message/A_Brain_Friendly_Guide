import requests, json

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)

data_dictionary = json.loads(response.text)
people_dictionary = data_dictionary['people']

for name in people_dictionary:
    print(name)