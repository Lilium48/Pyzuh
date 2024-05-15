import requests
from errors import handle_errors

class Logtest:
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token

    def run_logtest(self, token: str, log_format: str, location: str, event: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Run the logtest tool to check if a specified log raises any alert.

        Parameters:
        token (str): Token for the logtest session.
        log_format (str): Format of the log. Required. Allowed values: syslog, json, snort-full, squid, eventlog, eventchannel, audit, mysql_log, postgresql_log, nmapg, iis, command, full_command, djb-multilog, multi-line.
        location (str): Path to the log file. Required.
        event (str): Event to look for. Required.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: A dictionary containing the response from running the logtest tool.
        """

        # Define the endpoint URL
        endpoint = f"{self.api_url}/logtest"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Create the request body
        request_body = {
        "token": token,
        "log_format": log_format,
        "location": location,
        "event": event
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a POST request to the endpoint with the request body
        response = requests.post(endpoint, headers=headers, json=request_body, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def end_logtest_session(self, token: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Delete the saved logtest session corresponding to the specified token.

        Parameters:
        token (str): Token of the logtest saved session. Required.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: A dictionary containing the response from ending the logtest session.
        """

        # Define the endpoint URL
        endpoint = f"{self.api_url}/logtest/sessions/{token}"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        }

        # Send a DELETE request to the endpoint
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()