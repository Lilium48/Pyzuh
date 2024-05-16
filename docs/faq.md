# FAQ 
## How to make a request with Pyzuh? 
Wazuh uses jwt to make requests to the api. The following code is how you make a request using Pyzuh to the Wazuh API: 
```Python 
from pyzuh import Overview 

# Define your API URL and JWT token
api_url = "https://host-ip:55000.com"
jwt_token = "your-jwt-token"

# Create an instance of the Overview class
overview_client = Overview(api_url, jwt_token)

# Make a request to get agents overview
try:
    response = overview_client.get_agents_overview(pretty=True, wait_for_complete=False)
    print("Agents Overview:", response)
except ValueError as e:
    print("Error:", e) 
```
## Why is syscollector and vulnerability not available? 
Version 4.7 deprecated vulnerability. The functions for Syscollector can be found in experimental.

## How do I set environment variables? 
In the authentication portion of Pyzuh, I have included a way to set environmental variables for your username & password. See below of the basic syntax: 
```Python
import os

os.environ["WAZUH_USERNAME"] = "your_username"
os.environ["WAZUH_PASSWORD"] = "your_password"
```
You can create a function to store this and then call it when needed: 
```Python
def set_credentials():
    """
    Set Wazuh API username and password as environment variables.
    """
    username = input("Enter Wazuh API username: ")
    password = input("Enter Wazuh API password: ")
    
    os.environ["WAZUH_USERNAME"] = username
    os.environ["WAZUH_PASSWORD"] = password

    print(set_credentials)
```

## How do I authenticate? 
Here is a basic script to authenticate. JWT have a duration of 900 seconds. 
```Python
def authenticate(api_url: str) -> str:
    """
    Authenticate with the Wazuh API and return the JWT token.

    Args:
        api_url (str): The base URL for the Wazuh API.

    Returns:
        str: The JWT token.
    """
    set_credentials()
    try:
        # Authenticate with Wazuh API
        token = authenticate_wazuh(api_url)
        print("Authentication successful.")
        return token
    except Exception as e:
        print("Authentication failed:", e)
        return None
```