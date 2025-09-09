
from flask import Flask, request
import requests

app = Flask(__name__)

# -----------------------
# Homepage
# -----------------------
@app.route("/")
def home():
    return """
    <h2>Welcome to My Weather Website!</h2>
    <p>Click on this <a href='/about'>here</a> to go to the About page.</p>
    <p>Click on this <a href='/contact'>here</a> to go to the Contact page.</p>
    <p>Click on this <a href='/weather'>here</a> to go to the Weather Prediction page.</p>
    """

# -----------------------
# About Page
# -----------------------
@app.route("/about")
def about_page():
    return """
    <h2>About Page</h2>
    <p>Hello, and welcome to my page that predicts weather for the next 7 days like any other weather website.</p>
    <p><a href='/'>Back to Home</a></p>
    """

# -----------------------
# Contact Page
# -----------------------
@app.route("/contact")
def contact_page():
    return """
    <h2>Contact Page</h2>
    <p>You can contact us at freyn_lucas@student.mahoningctc.com.</p>
    <p><a href='/'>Back to Home</a></p>
    """

# -----------------------
# Weather Input Page
# -----------------------
@app.route("/weather")
def weather_page():
    return """
    <h2>Weather Prediction</h2>
    <p>Enter your city below to see a 7-Day forecast:</p>
    <form action="/weather_result" method="get">
        <input type="text" name="city" placeholder="Enter your city" required>
        <input type="submit" value="Get Forecast">
    </form>
    <p><a href='/'>Back to Home</a></p>
    """

# -----------------------
# Weather Result Page (7-Day Forecast using JSON)
# -----------------------
@app.route("/weather_result")
def weather_result():
    city = request.args.get("city")
    
    # Use wttr.in JSON format
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"<p>Could not get weather for {city}. <a href='/weather'>Try again</a></p>"
    
    data = response.json()
    forecast_days = data['weather']  # list of days
    
    forecast_html = "<ul>"
    for day in forecast_days:
        date = day['date']
        max_temp = day['maxtempF']
        min_temp = day['mintempF']
        desc = day['hourly'][4]['weatherDesc'][0]['value']  # approximate midday description
        forecast_html += f"<li>{date}: {desc}, {min_temp}°F - {max_temp}°F</li>"
    forecast_html += "</ul>"
    
    return f"""
    <h2>7-Day Weather Forecast for {city.title()}</h2>
    {forecast_html}
    <p><a href='/weather'>Back to Weather Page</a></p>
    <p><a href='/'>Back to Home</a></p>
    """

# -----------------------
# Run the Flask app
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
