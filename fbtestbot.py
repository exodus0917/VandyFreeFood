from flask import Flask, request
import requests
import sys
import os
import json
from Credentials import *
from AnsweringMachine import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
        return request.args.get('hub.challenge', 200)
    else:
        return 'Error, wrong validation token'


@app.route('/', methods=['POST'])
def handle_messages():
    data = request.get_json()
    log(data)

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                # can get incoming information from messaging_event
                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["mess4age"]["text"]
                    # @@@@@@@@catch the payload here@@@@@@@@@@@

                    # Need to interpret the message_text (use the interpreter pattern)
                    # Create an AnsweringMachine instance with the message_text as a param
                    #   then call the answer method to get the appropriate answer

                    # this code echos what the user says
                    # send_message(sender_id, message_text)

                    temp = AnsweringMachine(message_text)
                    send_message(sender_id, temp.answer())
                    # send_button_message(sender_id, 'Lets go to naver!')
                    # app.post('/webhook/')


                if messaging_event.get("delivery"):
                    pass

                if messaging_event.get("optin"):
                    pass

                if messaging_event.get("postback"):
                    pass

    return "ok", 200

# This method will send a string to the recipient
# @param recipient ID and a string
def send_message(recipient_id, message_text):
    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    })

    # posts the given string to the messenger
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
    log(r.text)

def send_button_message(recipient_id, text):
    buttons = [
        {
            'type': 'web_url',
            'url': 'http://www.naver.com/',
            'title': 'Show Naver'
        },
        {
            'type': 'postback',
            'title': 'Checking',
            'payload': 'I am the payload!'

        }
    ]
    # send_message(recipient_id, {
    #     "attachment": {
    #         "type": "template",
    #         "payload": {
    #             "template_type": "button",
    #             "text": text,
    #             "buttons": buttons
    #         }
    #     }
    # })

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": text,
                "buttons": buttons
            }
        }
    }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
    log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
