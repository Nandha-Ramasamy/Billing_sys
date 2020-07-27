def message_send(name,ph_no):
    import twilio
    from twilio.rest import Client
    num="+91"+ph_no
    message="Hello "+name+"\n Wish you a many more happy return of the day ,special offers are waiting for you"
    client=Client("AC3955bf1f432a881e7996b9bacc6250ac","45369c20b52c5bc29213e50f3079b888")
    client.messages.create(to=num,from_="+17752009599",body=message)
    print("Message sent,Done!")
