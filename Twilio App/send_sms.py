# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACdb899526b6219ab64aeb0722960c45dc'
auth_token = '31694f8689d1a4f4a2ec996806e247e4'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hello Your Project !',
         from_='+12563914676',
         to='+917039986165'
     )

print(message.sid)
