import os
from twilio.rest import Client

contatos = [""]

for contato in contatos:
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    client.messages.create(
        to=contato,  #nao pode ser trial para mandar SMS para outros numeros sem ser o seu
        from_='',
        body= "",
        media_url=[''] 
    )
