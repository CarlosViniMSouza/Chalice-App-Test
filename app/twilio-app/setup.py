from msilib.schema import CheckBox
from chalice import Chalice, Response
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from os import environ as env

# Configuration of Twilio:
AUTH_TOKEN = env.get('AUTH_TOKEN')
FROM_NUM = env.get('FROM_NUM')
ACC_SID = env.get('ACC_SID')
TO_NUM = env.get('TO_NUM')

app = Chalice(app_name='sms-shot')

twilio_client = Client(ACC_SID, AUTH_TOKEN)


@app.route('/service/sms/send', methods=['POST'])
def send_sms():
    request_body = app.current_request.json_body
    if request_body:
        try:
            msg = twilio_client.messages.create(
                from_=FROM_NUM,
                body=request_body['msg'],
                to=TO_NUM)

            if msg.sid:
                return Response(status_code=201,
                                headers={
                                    'Content-Type': 'application/json'
                                },
                                body={
                                    'status': 'success',
                                    'data': msg.sid,
                                    'message': 'SMS successfully sent'
                                })
            else:
                return Response(status_code=200,
                                headers={
                                    'Content-Type': 'application/json'
                                },
                                body={
                                    'status': 'failure',
                                    'message': 'Please try again!!!'
                                })

        except TwilioRestException as exc:
            return Response(status_code=400,
                            headers={'Content-Type': 'application/json'}, body={
                                'status': 'failure',
                                'message': exc.msg})
