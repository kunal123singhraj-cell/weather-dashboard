from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY = "bd5e378503939ddaee76f12ad7a97608"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-weather", methods=["POST"])
def get_weather():
    data = request.get_json()
    city = data.get("city")
    
    if not city:
        return jsonify({"error": "Please enter a city name."}), 400
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "City not found. Please check the spelling."}), 404
        
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, port=5002)