from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Smart Home API"

@app.route('/alexa', methods=['POST'])
def alexa():
    data = request.json
    intent = data['request']['intent']['name']
    
    if intent == 'TurnOnLightsIntent':
        # Logic to turn on the lights
        response_text = "Encendiendo la luz."
        return jsonify(build_response(response_text))
    else:
        return jsonify(build_response("Intento desconocido")), 400

def build_response(output):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output,
            },
            'shouldEndSession': True,
        }
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3838)