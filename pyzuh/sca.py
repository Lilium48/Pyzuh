import requests
from errors import handle_errors

class Sca: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    def get_sca_results(self, agent_id: str, pretty: bool = False, wait_for_complete: bool = False, name: str = None, description: str = None, references: str = None, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list = None, q: str = None, distinct: bool = False) -> dict:
        """
        Return the security SCA database of an agent.

        Parameters:
        agent_id (str): Agent ID. All possible values from 000 onwards.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        name (str, optional): Filter by policy name.
        description (str, optional): Filter by policy description.
        references (str, optional): Filter by references.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (list, optional): Select which fields to return (separated by comma). Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: The security SCA database of the specified agent.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/sca/{agent_id}"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "name": name,
            "description": description,
            "references": references,
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "search": search,
            "select": select,
            "q": q,
            "distinct": str(distinct).lower()
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_policy_checks(self, agent_id: str, policy_id: str, pretty: bool = False, wait_for_complete: bool = False, title: str = None, description: str = None, rationale: str = None, remediation: str = None, command: str = None, reason: str = None, file: str = None, process: str = None, directory: str = None, registry: str = None, references: str = None, result: str = None, condition: str = None, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list = None, q: str = None, distinct: bool = False) -> dict:
        """
        Return the policy monitoring alerts for a given policy.

        Parameters:
        agent_id (str): Agent ID. All possible values from 000 onwards.
        policy_id (str): Filter by policy id.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        title (str, optional): Filter by title.
        description (str, optional): Filter by policy description.
        rationale (str, optional): Filter by rationale.
        remediation (str, optional): Filter by remediation.
        command (str, optional): Filter by command.
        reason (str, optional): Filter by reason.
        file (str, optional): Filter by full path.
        process (str, optional): Filter by process name.
        directory (str, optional): Filter by directory.
        registry (str, optional): Filter by registry.
        references (str, optional): Filter by references.
        result (str, optional): Filter by result.
        condition (str, optional): Filter by condition.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (list, optional): Select which fields to return (separated by comma). Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: The policy monitoring alerts for the specified policy.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/sca/{agent_id}/checks/{policy_id}"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "title": title,
            "description": description,
            "rationale": rationale,
            "remediation": remediation,
            "command": command,
            "reason": reason,
            "file": file,
            "process": process,
            "directory": directory,
            "registry": registry,
            "references": references,
            "result": result,
            "condition": condition,
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "search": search,
            "select": select,
            "q": q,
            "distinct": str(distinct).lower()
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()