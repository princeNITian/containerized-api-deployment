from flask import Blueprint, jsonify, request

# Create a Flask Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Default route."""
    return jsonify({"message": "Welcome to the Flask API!"})

@main.route('/weather', methods=['GET'])
def get_weather():
    """
    Mock route for fetching weather.
    (You can integrate an external API like OpenWeatherMap here.)
    """
    city = request.args.get('city', 'unknown')
    return jsonify({
        "city": city,
        "temperature": "22°C",
        "status": "Sunny"
    })
