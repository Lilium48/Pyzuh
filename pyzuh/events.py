import requests 
from errors import handle_errors

class Events: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def ingest_events(self, events: list, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Send security events to analysisd.

        Parameters:
        events (list): Bulk of events to send. Ensure you follow the limits of 30 requests per minute and 100 events per request.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The response from the server after ingesting the events.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/events"

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

        # Send a POST request to the endpoint with the events as a JSON payload
        response = requests.post(endpoint, headers=headers, params=params, json={"events": events})

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
