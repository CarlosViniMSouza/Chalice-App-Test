from multiprocessing.connection import Client
from os import environ as env
from twilio.rest import Client

# Configuration of Twilio:
AUTH_TOKEN = env.get('AUTH_TOKEN')
FROM_NUM = env.get('FROM_NUM')
ACC_SID = env.get('ACC_SID')
TO_NUM = env.get('TO_NUM')

twilio_client = Client(ACC_SID, AUTH_TOKEN)


def send(payload_params=None):
    msg = twilio_client.messages.create(
        from_=FROM_NUM,
        body=payload_params['msg'],
        to=TO_NUM
    )

    if msg.sid:
        return msg
