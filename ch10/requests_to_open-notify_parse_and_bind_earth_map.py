import requests, json, turtle

def move_iss(long, lat):
    global iss
    iss.penup()
    iss.goto(long, lat)
    iss.pendown()

screen = turtle.Screen()
screen.setup(1000, 500)
screen.bgpic('earth.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
turtle.register_shape('iss.gif')
iss.shape('iss.gif')

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if ( response.status_code == 200 ):
    response_dictionay = json.loads(response.text)
    iss_position = response_dictionay['iss_position']
    print("International Space Station at "
            + iss_position['longitude']
            + ", "
            + iss_position['latitude'])
            
    long = float(iss_position['longitude'])
    lat = float(iss_position['latitude'])
    move_iss(long, lat)

else:
    print("Houston, we have a problem: ", response.status_code)

turtle.mainloop()