import requests
from errors import handle_errors

class Tasks:
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token

    def list_tasks(self, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, q: str = None,
                   search: str = None, select: list = None, sort: str = None, agents_list: list = None, tasks_list: list = None,
                   command: str = None, node: str = None, module: str = None, status: str = None) -> dict:
        """
        Returns all available information about the specified tasks.

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
            offset (int, optional): First element to return in the collection. Must be >= 0. Defaults to 0.
            limit (int, optional): Maximum number of elements to return. Recommended not to exceed 500. Defaults to 500.
            q (str, optional): Query to filter results by. For example, q="status=active". Defaults to None.
            search (str, optional): Look for elements containing the specified string. Use '-' at the beginning for complementary search. Defaults to None.
            select (list, optional): List of fields to return (comma-separated string). Use '.' for nested fields (e.g., 'field1.field2'). Defaults to None.
            sort (str, optional): Criteria for sorting the results. Use +/- at the beginning for ascending/descending order. Use '.' for nested fields. Defaults to None.
            agents_list (list, optional): List of agent IDs (comma-separated). All agents are selected by default if not specified. Defaults to None.
            tasks_list (list, optional): List of task IDs (comma-separated). Defaults to None.
            command (str, optional): Filter results by command. Defaults to None.
            node (str, optional): Filter results by node. Defaults to None.
            module (str, optional): Filter results by module. Defaults to None.
            status (str, optional): Filter results by status. Defaults to None.

        Returns:
            dict: A dictionary containing information about the specified tasks.
            """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/tasks"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "offset": str(offset),
            "limit": str(limit),
            "q": q,
            "search": search,
            "select": ",".join(select) if select else None,
            "sort": sort,
            "agents_list": ",".join(agents_list) if agents_list else None,
            "tasks_list": ",".join(tasks_list) if tasks_list else None,
            "command": command,
            "node": node,
            "module": module,
            "status": status
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
