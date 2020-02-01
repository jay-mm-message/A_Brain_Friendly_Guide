import requests, json

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if ( response.status_code == 200 ):
    response_dictionay = json.loads(response.text)
    iss_position = response_dictionay['iss_position']
    print("International Space Station at "
            + iss_position['longitude']
            + ", "
            + iss_position['latitude'])
else:
    print("Houston, we have a problem: ", response.status_code)