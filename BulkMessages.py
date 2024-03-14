from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# List of recipients with their WhatsApp numbers
recipients = {
    'Recipient 1': 'whatsapp:+916266061914',
    'Recipient 2': 'whatsapp:+919826477767',
    # Add more recipients as needed
}

# Message to send
message_body = 'hello world!'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send messages to each recipient
for name, number in recipients.items():
    try:
        message = client.messages.create(
            body=message_body,
            from_='whatsapp:+14155238886',  # Twilio's WhatsApp sandbox number
            to=number
        )
        print(f"Message sent to {name} at {number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {name} at {number}: {str(e)}")
