from flask import Blueprint, render_template, request
import datetime as dt
import requests
views = Blueprint(__name__ ,"views")

API_KEY = "e91d2750d685599e6e19f07f9d3523ce"
ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
APP_ID = "e91d2750d685599e6e19f07f9d3523ce"
UNITS = "metric"

# url_lan_lat = "https://api.openweathermap.org/data/2.5/weather?lat=51.5072&lon=0.1276&appid=e91d2750d685599e6e19f07f9d3523ce"
# url_city_country = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=e91d2750d685599e6e19f07f9d3523ce"
# response = requests.get(url_city_country).json()


##def formula():
   ## (["temp"] - 32) * 5/9 
##temp_c = formula


@views.route("/", methods = ["GET","POST"])

def home():
    response = request.form.get("city-request")
    city = response
    url = build_weather_link(city)
    response = requests.get(url)
    data = response.json()
    weather_name = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    wind = data["wind"]["speed"] 

                
    return render_template("index.html", city=city, weather_name =  weather_name, temp=temp, wind = wind)

def build_weather_link(city):
    return f"{ENDPOINT}?q={city}&appid={APP_ID}&units={UNITS}"

@views.route("/startpage")
def startpage():
    return "<p>.</p>"

@views.route("/news")
def news():
    return "<p>.</p>"

@views.route("/about")
def about():
    return "<p>.</p>"

@views.route("/contact")
def contact():
    return "<p>.</p>"

