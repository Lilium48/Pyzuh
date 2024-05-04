import requests 
import logging 
import os 

def authenticate_wazuh(api_url: str, username: str, password: str) -> str:
    """
    Authenticate with the Wazuh API and obtain a JWT token.

    Parameters:
    - api_url (str): The base URL for the Wazuh API (e.g. "https://<HOST_IP>:55000").
    - username (str): The username for basic authentication.
    - password (str): The password for basic authentication.

    Returns:
    - str: The JWT token.

    Raises:
    - Exception: If the authentication request fails or the response is not as expected.
    """
    # Set the authentication URL
    auth_url = f"{api_url}/security/user/authenticate"

    # Make the POST request to authenticate
    try:
        response = requests.post(
            auth_url,
            auth=(username, password),
            verify=False  # Disable SSL verification if needed (change to True for secure connections)
        )

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extract the token from the response data
            jwt_token = data.get("data", {}).get("token")
            if jwt_token:
                return jwt_token
            else:
                raise Exception("JWT token not found in the response data.")
        else:
            # Log an error and raise an exception for non-200 status codes
            logging.error(f"Authentication failed with status code {response.status_code}: {response.text}")
            response.raise_for_status()
    except Exception as e:
        # Handle any other exceptions and log an error message
        logging.error(f"An error occurred during authentication: {e}")
        raise

# Example usage:
# api_url = "https://<HOST_IP>:55000"
# username = "<YOUR_USERNAME>"
# password = "<YOUR_PASSWORD>"
# token = authenticate_wazuh(api_url, username, password)
# print("JWT Token:", token)
