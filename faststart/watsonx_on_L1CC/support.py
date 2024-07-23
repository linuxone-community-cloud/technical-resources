# Assisted by WCA@IBM
# Latest GenAI contribution: ibm/granite-20b-code-instruct-v2
import requests

# Set up your API credentials and service URL
# TIP: in our setup, connection to assistant is happening through the proxy to introduce requests rate limiting.
SERVICE_URL = 'https://community.ibm.com/zsystems/api/l1cc/assistant'
API_VERSION = '2023-06-15'
ASSISTANT_ID = '98479e76-2510-4894-a9e2-7750bb9d21d9'

# The color class is a utility class that provides constants for various colors and formatting options supported by terminal emulators. It can be used to colorize text output in Python scripts or applications.
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# The `send_message` function is used to send a message to the Assistant instance and retrieve the response.
def send_message(message):
    headers = {
        'Content-Type': 'application/json'
    }

    # Define the payload for the API call
    payload = {
        'input': {
            'text': message
        }
    }

    # Make the API call
    response = requests.post(SERVICE_URL + '/v2/assistants/' + ASSISTANT_ID + '/message?version=' + API_VERSION,
                            headers=headers, json=payload)
    
    return response.json()

print(color.BOLD + '\nWelcome to IBM LinuxONE Community Cloud support assistant'+ color.END + '\n\nI am here to assist you with any issues or questions you may have while using the IBM LinuxONE Community Cloud.\n\nTo get started, please tell me what you would like to do. You can ask me things like:\n' + color.CYAN + '\n- How can I determine what kernel level?\n- How can I find out how much cpu and memory my server is using?\n- How do I switch to the root user?\n- How can I see how much disk space is left?' + color.END + '\n\nI will do my best to provide you with the information or assistance you need. If you need more assistance, feel free to ask!\n\n' + color.CYAN + 'TIP: ' + color.END + 'Type \'exit\' to close the session\n')    

# Keep asking for messages until the user says 'exit'
while True:
    # Get the user input
    message = input(color.GREEN + 'You: ' + color.END)

    # Check if user wants to end the conversation
    if message.lower() == 'exit':
        break

    # Send the message to watsonx Assistant
    response = send_message(message)

    # Provide a formatted reply from the watsonx Assistant
    print(color.BLUE + 'watsonx: ' + color.END + response['output']['generic'][0]['text'] + '\n')


print (color.BOLD + '\nThank you for using IBM LinuxONE Community Cloud support assistant' + color.END + '\n')

