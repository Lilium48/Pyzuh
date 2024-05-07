import requests
import json
from errors import handle_errors

class ActiveResponse:
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token

    def run_command(self, data, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Send a PUT request to the Active Response API.

        Parameters:
            data (dict): The data to send in the request body.
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
            dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/active-response"
        
        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a PUT request to the API
        response = requests.put(endpoint, headers=headers, params=params, data=json.dumps(data))

        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
