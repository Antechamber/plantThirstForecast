from flask import Flask
import json
import requests
from datetime import datetime, timedelta

app = Flask(__name__, static_url_path='')

# configuration
apiKey = "aa681fd562b24ade8df211830242906"
zipCode = "98229"


@app.route('/')
def home():
    return app.send_static_file("index.html")


@app.route("/current")
def current():
    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json?q={zipCode}&key={apiKey}")
    return json.loads(response.text)


@app.route("/forecast")
def current():
    response = requests.get(
        f"https://api.weatherapi.com/v1/forecast.json?q={zipCode}&days=3&key={apiKey}")
    return json.loads(response.text)


@app.route("/historical")
def current():
    todaysDate = datetime.now().strftime("%Y-%m-%d")
    threeDaysAgo = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
    response = requests.get(
        f"https://api.weatherapi.com/v1/history.json?q={zipCode}&dt={todaysDate}&end_dt={threeDaysAgo}&key={apiKey}")
    return json.loads(response.text)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
