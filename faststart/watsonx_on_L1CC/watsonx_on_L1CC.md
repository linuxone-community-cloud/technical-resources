# IBM watsonx Assistant Fast Start guide for IBM LinuxONE Community Cloud

## Introduction

In this guide, you'll learn how to create a Python script that connects to IBM watsonx Assistant, IBM's AI-powered chatbot service. This chatbot will answer common user questions about the LinuxONE Community Cloud. You can choose from three different options to complete this guide, depending on your preferences and experience level:

- **Option 1:** [Quick demo with pre-built script](#option-1) (Easiest)
- **Option 2:** [Focus on Python development with existing IBM watsonx Assistant instance for IBM LinuxONE Community Cloud](#option-2) (Intermediate)
- **Option 3:** [The complete development flow, including creation of your own IBM watsonx Assistant instance](#option-3) (Most Comprehensive)

<a id="option-1"></a>

## [Option 1] Quick demo with pre-built script (Easiest)

### Option 1 prerequisites

- Access to the [LinuxONE Community Cloud VM instance](https://github.com/linuxone-community-cloud/technical-resources/blob/master/faststart/deploy-virtual-server.md)
- A Linux terminal or SSH client

#### Open a terminal or SSH client and connect to your LinuxONE Community Cloud VM

```bash
ssh –i /path/to/key/keyname.pem linux1@serveripaddress
```

_TIP: you can find details about how to obtain your SSH key or server IP address in [Virtual Server Deployment Guide](https://github.com/linuxone-community-cloud/technical-resources/blob/master/faststart/deploy-virtual-server.md)_

#### Use curl to download the pre-built Python script from the GitHub

```bash
curl -O https://raw.githubusercontent.com/andriivasylchenko/l1cc-support-assistant-guide/main/support.py
```

#### Run the IBM LinuxONE Community Cloud support assistant

```bash
python3 support.py
```

_TIP: try to ask the assistant "how to get started?"_

<a id="option-2"></a>

## [Option 2] Python script development with existing IBM watsonx Assistant instance for IBM LinuxONE Community Cloud

### Option 2 prerequisites

- A code editor (Visual Studio Code, Atom or etc)
- Basic Python knowledge (helpful, but not required)
- Access to the [LinuxONE Community Cloud VM instance](https://github.com/linuxone-community-cloud/technical-resources/blob/master/faststart/deploy-virtual-server.md)
- A Linux terminal or SSH client

#### Create a new Python file

Create a new file named `support.py` using a code editor of your choice.

#### Import the requests library

```python
import requests
```

This line imports the `requests` library, which we'll use to communicate with the IBM watsonx Assistant API over the internet.

#### Define variables

Add the following lines to the script

```python
SERVICE_URL = 'https://community.ibm.com/zsystems/api/l1cc/assistant'
API_VERSION = '2023-06-15'
ASSISTANT_ID = '98479e76-2510-4894-a9e2-7750bb9d21d9'
```

These lines store important information:

- SERVICE_URL: The address of the IBM watsonx Assistant API endpoint.
- API_VERSION: The version of the API you'll be using.
- ASSISTANT_ID: The unique identifier for your IBM watsonx Assistant instance.

_TIP: With Option 2, you will leverage a proxy URL that allows IBM LinuxONE Community Cloud team to control the requests throughput. If you want to establish direct connection with IBM watsonx Assistant API, please follow [Option 3](#option-3)._

#### Create the send_message function

Type or paste the following function

```python
def send_message(message):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'input': {
            'text': message
        }
    }
    response = requests.post(SERVICE_URL + '/v2/assistants/' + ASSISTANT_ID + '/message?version=' + API_VERSION, headers=headers, json=payload)
    return response.json()
```

- This function takes a message (text input from the user) as input.
- It constructs an HTTP request to the IBM watsonx Assistant API with the user's message.
- The request includes necessary headers.
- The response from the API (the IBM watsonx Assistant answer) is returned as a JSON object.

#### (Optional) Add colors to terminal output

If you want to add color to the terminal output, you can include the color class.

```python
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
```

You can then use class methods to colorize text output in the console, for example:

```python
print(color.PURPLE + 'This is purple text!' + color.END)
```

#### Create the chat interface

```python
print("Welcome to IBM LinuxONE Community Cloud support assistant\n")

while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break

    response = send_message(message)
    print("watsonx: " + response['output']['generic'][0]['text'] + '\n')

print("\nThank you for using IBM LinuxONE Community Cloud support assistant\n")
```

This code creates a loop that:

- Prompts the user to type a message (You:).
- If the user types "exit", the loop ends.
- Otherwise, it sends the message to the send_message function to get the chatbot's response.
- Prints the chatbot's response to the terminal.

#### Connect to your LinuxONE Community Cloud VM

Use terminal or or SSH client to connect to your Virtual Server on IBM LinuxONE Community Cloud

```bash
ssh –i /path/to/key/keyname.pem linux1@serveripaddress
```

_TIP: you can find details about how to obtain your SSH key or server IP address in [Virtual Server Deployment Guide](https://github.com/linuxone-community-cloud/technical-resources/blob/master/faststart/deploy-virtual-server.md)_

#### Transfer the script to VM

Using your editor of choice (e.g. vim, nano, etc) save `support.py` script to the VM.

#### Launch the IBM LinuxONE Community Cloud support assistant

```bash
python3 support.py
```

_TIP: try to ask the assistant "how to get started?"_

<a id="option-3"></a>

## [Option 3] Setup your own IBM watsonx Assistant instance and develop a Python script to work with it through APIs

### Option 3 prerequisites

- A code editor (Visual Studio Code, Atom or etc)
- Basic Python knowledge (helpful, but not required)
- [IBM Cloud account](https://cloud.ibm.com/docs/account?topic=account-account-getting-started)
- [IBM watsonx Assistant paid plan](https://cloud.ibm.com/login?state=%2Fdeveloper%2Fwatson%2Flaunch-tool%2Fconversation) (API access is not avaliable on Lite or Trial plan)
- Access to the [LinuxONE Community Cloud VM instance](https://github.com/linuxone-community-cloud/technical-resources/blob/master/faststart/deploy-virtual-server.md)
- A Linux terminal or SSH client

#### Create your IBM watsonx Assistant instance

Follow the [instance creation process](https://cloud.ibm.com/login?state=%2Fdeveloper%2Fwatson%2Flaunch-tool%2Fconversation) and select a Paid plan.

#### Building an action in IBM watsonx Assistant

Follow the [video tutorial](https://vimeo.com/814318967) to learn and build your first action in IBM watsonx Assistant.

_TIP: don't forget to publish your changes to a live environment. You can find more guidance and video tutorials in your IBM watsonx Assistant instance dashboard_

#### Obtain API Key and Service URL

In your IBM Cloud account, navigate to your IBM watsonx Assistant instance.
Note down the Assistant ID, generate an API key, and get the Service URL.

#### Create a new file

Create a new file named `assistant.py` using a code editor of your choice.

#### Import the library

```python
import requests
```

This line imports the `requests` library, which we'll use to communicate with the IBM watsonx Assistant API over the internet.

#### Define assistant variables

Add the following lines to the script

```python
SERVICE_URL = 'YOUR_ASSISTANT_SERVICE_URL'
API_KEY = 'YOUR_ASSISTANT_API_KEY'
API_VERSION = '2023-06-15'
ASSISTANT_ID = 'YOUR_ASSISTANT_SERVICE_URL'
```

These lines store important information:

- SERVICE_URL: The address of the IBM watsonx Assistant API endpoint.
- API_KEY: Your authentication key to access the service.
- API_VERSION: The version of the API you'll be using.
- ASSISTANT_ID: The unique identifier for your IBM watsonx Assistant instance.

#### Create a function to send API request

Type or paste the following function

```python
def send_message(message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + API_KEY
    }
    payload = {
        'input': {
            'text': message
        }
    }
    response = requests.post(SERVICE_URL + '/v2/assistants/' + ASSISTANT_ID + '/message?version=' + API_VERSION, headers=headers, json=payload)
    return response.json()
```

- This function takes a message (text input from the user) as input.
- It constructs an HTTP request to the IBM watsonx Assistant API with the user's message.
- The request includes necessary headers.
- The response from the API (the IBM watsonx Assistant answer) is returned as a JSON object.

#### (Optional) Create and use color class to improve terminal output

If you want to add color to the terminal output, you can include the color class.

```python
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
```

You can then use class methods to colorize text output in the console, for example:

```python
print(color.PURPLE + 'This is purple text!' + color.END)
```

#### Create the script interface

```python
print("Welcome to IBM watsonx Assistant\n")

while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break

    response = send_message(message)
    print("watsonx: " + response['output']['generic'][0]['text'] + '\n')

print("\nThank you for using IBM watsonx Assistant\n")
```

This code creates a loop that:

- Prompts the user to type a message (You:).
- If the user types "exit", the loop ends.
- Otherwise, it sends the message to the send_message function to get the chatbot's response.
- Prints the chatbot's response to the terminal.

#### Connect to your LinuxONE Community Cloud Virtual Machine

Use terminal or or SSH client to connect to your Virtual Server on IBM LinuxONE Community Cloud

```bash
ssh –i /path/to/key/keyname.pem linux1@serveripaddress
```

_TIP: you can find details about how to obtain your SSH key or server IP address in [Virtual Server Deployment Guide](https://github.com/linuxone-community-cloud/technical-resources/blob/master/faststart/deploy-virtual-server.md)_

#### Transfer the script to your LinuxONE Community Cloud VM

Using your editor of choice (e.g. vim, nano, etc) save `assistant.py` script to the VM.

#### Launch and test your assistant

```bash
python3 assistant.py
```

_TIP: use your created IBM watsonx Assistant action prompt_

