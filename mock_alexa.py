import requests
import json

# URL of the Flask application
url = 'http://localhost:3838/alexa'

# Mock payload for the "TurnOffLightsIntent"
payload = {
    "version": "1.0",
    "session": {
        "new": True,
        "sessionId": "amzn1.echo-api.session.123456789012",
        "application": {
            "applicationId": "amzn1.ask.skill.123456789012"
        },
        "user": {
            "userId": "amzn1.ask.account.123456789012"
        }
    },
    "context": {
        "System": {
            "application": {
                "applicationId": "amzn1.ask.skill.123456789012"
            },
            "user": {
                "userId": "amzn1.ask.account.123456789012"
            },
            "device": {
                "deviceId": "amzn1.ask.device.123456789012",
                "supportedInterfaces": {}
            }
        }
    },
    "request": {
        "type": "IntentRequest",
        "requestId": "amzn1.echo-api.request.123456789012",
        "timestamp": "2020-03-22T22:59:59Z",
        "locale": "en-US",
        "intent": {
            "name": "TurnOffLightsIntent",
            "confirmationStatus": "NONE",
            "slots": {}
        }
    }
}

# Send the mock request to the Flask application
response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())