import requests
import jwt
import json
import logging

def active_response(api_url, jwt_token, agents_list=None, command=None, arguments=None, custom=False, alert=None, pretty=False, wait_for_complete=False):
    """
    Run an Active Response command on all agents or a list of them.

    Parameters:
    api_url (str): The base URL for the Active Response API.
    jwt_token (str): The JWT token for authentication.
    agents_list (list): A list of agent IDs to target. All agents will be targeted if not specified.
    command (str): The active response command to run.
    arguments (list): A list of arguments for the command.
    custom (bool): Whether the command is custom or not. Default is False.
    alert (dict): Alert options as a dictionary.
    pretty (bool): Whether to show results in a human-readable format. Default is False.
    wait_for_complete (bool): Whether to wait for command completion. Default is False.

    Returns:
    dict: The API response as a dictionary.
    """
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }

    # Prepare the request body
    body = {
        "command": command,
        "arguments": arguments,
        "custom": custom
    }

    if alert:
        body["alert"] = alert

    # Prepare query parameters
    params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
    }
    
    if agents_list:
        params["agents_list"] = ','.join(agents_list)

    # Make the request to the Active Response API
    response = requests.post(api_url, headers=headers, params=params, data=json.dumps(body))

    # Check the response status
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400: 
        print("Bad request")
    elif response.status_code == 401:
        print("Unauthorized Request")
    elif response.status_code == 403: 
        print("Permission Denied")
    elif response.status_code == 405: 
        print("Invalid HTTP Method")
    elif response.status_code == 406: 
        print("Invalid Content-Type")
    elif response.status_code == 413:
        print("Maximum request body size exceeded")
    elif response.status_code == 429:
        print("Maximum request per minute reached")
        
# Example usage:
# active_response(
#     api_url="https://your.api.url/active-response",
#     jwt_token="your-jwt-token",
#     agents_list=["1", "2", "3"],
#     command="!your-script-name",
#     arguments=["arg1", "arg2"],
#     custom=True,
#     alert={"some_alert_key": "some_alert_value"},
#     pretty=True,
#     wait_for_complete=True
# )
