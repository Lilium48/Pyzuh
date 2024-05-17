import os
from pyzuh import authenticate_wazuh
from pyzuh import Ciscat 

def set_credentials():
    """
    Set Wazuh API username and password as environment variables.
    """
    username = input("Enter Wazuh API username: ")
    password = input("Enter Wazuh API password: ")
    
    os.environ["WAZUH_USERNAME"] = username
    os.environ["WAZUH_PASSWORD"] = password

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

def main():
    # Set the base URL for the Wazuh API
    api_url = "https://<HOST_IP>:55000"

    # Authenticate with Wazuh API
    jwt_token = authenticate(api_url)
    if not jwt_token:
        return
    
    # Create an instance of Ciscat class
    ciscat = Ciscat(api_url, jwt_token)

    # Example: Get CIS-CAT results for a specific agent
    agent_id = "<AGENT_ID>"  # Replace <AGENT_ID> with the actual agent ID
    results = ciscat.get_results(agent_id)
    print("CIS-CAT Results:", results)

if __name__ == "__main__":
    main()
