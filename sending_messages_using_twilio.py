
from twilio.rest import Client

def send_msg():
    # Your Account SID from twilio.com/console
    account_sid = "ACc2e9f381a58e......................"
    # Your Auth Token from twilio.com/console
    auth_token  = "3fd4d393b72c......................."
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
            to="+447438........", 
            from_="+44124......",
            body="--new video received--")
