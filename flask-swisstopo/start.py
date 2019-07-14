from flask import Flask
from flask import render_template
import requests
import uuid
import os


app = Flask(__name__)

# http://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml
# <ows:LowerCorner>5.140242 45.398181</ows:LowerCorner>
# <ows:UpperCorner>11.47757 48.230651</ows:UpperCorner>

@app.route('/')
def hello_world():

    zoom = 19
    tilex = 30
    tiley = 49

    url = f"https://wmts6.geo.admin.ch/1.0.0/ch.swisstopo.swissimage/default/current/21781/{zoom}/{tilex}/{tiley}.jpeg"

    payload = ""
    headers = {
        'Origin': "https://www.uvek-gis.admin.ch",
        'cache-control': "no-cache",
    }

    response = requests.request("GET", url, data=payload, headers=headers)

    filename = f"temp/{zoom}-{tilex}-{tiley}.jpg"

    with open(filename, "wb") as image:
        image.write(response.content)

    cwd = os.getcwd()

    return render_template("index.html")




app.run(debug=True, host="localhost", port=5555)
