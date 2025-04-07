from flask import Flask, render_template, request, send_from_directory
import requests
import os

app = Flask(__name__, static_folder="static")

API_KEY = "f963fd795161441aa53151011253003"  # Replace with your actual API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None
    
    if request.method == "POST":
        city = request.form["city"].strip()
        if city:
            url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
            response = requests.get(url)
            if response.status_code == 200:
                weather_json = response.json()
                if "error" not in weather_json:
                    weather_data = {
                        "city": weather_json["location"]["name"],
                        "country": weather_json["location"]["country"],
                        "temperature": weather_json["current"]["temp_c"],
                        "humidity": weather_json["current"]["humidity"],
                        "condition": weather_json["current"]["condition"]["text"],
                        "icon": weather_json["current"]["condition"]["icon"]
                    }
                else:
                    error_message = "City not found. Please enter a valid city."
            else:
                error_message = "Failed to retrieve data. Try again later."
        else:
            error_message = "Please enter a city name."

    return render_template("index.html", weather=weather_data, error=error_message)

# Serve static files correctly
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, "static"), filename)

# WSGI Entry Point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)  # Debug mode is OFF in production
