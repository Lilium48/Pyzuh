import os
import requests

def authenticate_wazuh(api_url: str) -> str:
    """
    Authenticate with the Wazuh API and obtain a JWT token using credentials from environment variables.

    Parameters:
    - api_url (str): The base URL for the Wazuh API (e.g. "https://<HOST_IP>:55000").

    Returns:
    - str: The JWT token.

    Raises:
    - Exception: If the authentication request fails or the response is not as expected.
    """
    # Read the username and password from environment variables
    username = os.getenv("WAZUH_USERNAME")
    password = os.getenv("WAZUH_PASSWORD")
    if not username or not password:
        raise Exception("WAZUH_USERNAME and WAZUH_PASSWORD environment variables are not set.")

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
            # Raise an exception for non-200 status codes
            response.raise_for_status()
    except Exception as e:
        # Handle any exceptions
        raise Exception(f"Authentication failed: {e}")

# Example usage:
# api_url = "https://<HOST_IP>:55000"
# token = authenticate_wazuh(api_url)
# print("JWT Token:", token)
