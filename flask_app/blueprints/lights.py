from flask import Blueprint, request, jsonify

lights_blueprint = Blueprint('lights', __name__)

@lights_blueprint.route('/turn_off', methods=['POST'])
def turn_off_lights():
    # Implement logic to turn off the lights
    return jsonify({"response": "Lights turned off"}), 200

@lights_blueprint.route('/turn_on', methods=['POST'])
def turn_on_lights():
    # Implement logic to turn on the lights
    return jsonify({"response": "Lights turned on"}), 200