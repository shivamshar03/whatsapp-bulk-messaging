import pywhatkit

def send_whatsapp_message(numbers, message):
    for number in numbers:
        try:
            # Send message with reduced wait time (e.g., 10 seconds)
            pywhatkit.sendwhatmsg(number, message, 18, 13, wait_time=10)
            print(f"Message sent to {number}")
        except Exception as e:
            print(f"Failed to send message to {number}. Error: {str(e)}")

if __name__ == "__main__":
    # Input WhatsApp numbers and message
    numbers = input("Enter WhatsApp numbers (separated by comma): ").split(",")
    message = input("Enter the message you want to send: ")

    # Remove leading/trailing whitespaces from numbers
    numbers = ["+91"+number.strip() for number in numbers]

    # Call function to send WhatsApp message
    send_whatsapp_message(numbers, message)
