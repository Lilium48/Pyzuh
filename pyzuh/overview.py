import requests
from errors import handle_errors

class Overview: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
        
    def get_agents_overview(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return a dictionary with a full agent overview. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/overview/agents"

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

        # Send a put request. 
        response = requests.put(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)