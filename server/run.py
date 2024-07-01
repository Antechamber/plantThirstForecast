from flask import Flask
import json
import requests

app = Flask(__name__, static_url_path='')

# configuration
apiKey = "aa681fd562b24ade8df211830242906"
zipCode = "98229"
currentWeatherURL = f"https://api.weatherapi.com/v1/current.json?q={zipCode}&key={apiKey}"


@app.route('/')
def home():
    return app.send_static_file("index.html")


@app.route("/current")
def current():
    res = requests.get(currentWeatherURL)
    return json.loads(res.text)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
