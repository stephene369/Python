from twilio.rest import Client

# Vos identifiants Twilio
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# Le numéro que vous souhaitez appeler
to_number = '+22960877728'

# Le numéro Twilio à partir duquel vous souhaitez passer l'appel
from_number = '+22996049621'

# Le message que vous souhaitez lire à haute voix
message = 'Bonjour, ceci est un appel de test.'

# Passer l'appel
call = client.calls.create(
    twiml='<Say>{}</Say>'.format(message),
    to=to_number,
    from_=from_number
)

print(call.sid)