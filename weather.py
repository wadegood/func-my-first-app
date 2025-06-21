import requests

class Weather:
    def __init__(self, temperature, conditions, events):
        self.temperature = temperature
        self.conditions = conditions
        self.events = events

    def __str__(self):
        return f"Temperature: {self.temperature}°F, Conditions: {self.conditions}, Events: {self.events}"

    def get_weather():
        url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/san%20Diego?unitGroup=us&include=events&key=6D7V3727GDNLXUKXHJAVZPBAJ&contentType=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        current = data['days'][0]
        temperature = current.get('temp', 'N/A')
        conditions = current.get('conditions', 'N/A')
        events = current.get('events', [])
        return Weather(temperature, conditions, events)

# Example usage:
if __name__ == "__main__":
    weather = Weather.get_weather()
    print(weather)