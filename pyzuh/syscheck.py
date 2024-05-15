import requests
from errors import handle_errors

class Syscheck: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def run_sysscan(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list = None) -> dict:
        """
        Send a PUT request to the sysscan API to run a rootcheck scan.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        agents_list (list of str, optional): List of agent IDs to target the scan. Defaults to None (run on all agents).

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/syscheck"
    
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

        # If agents_list is provided, add it to the query parameters
        if agents_list:
            params["agents_list"] = ",".join(agents_list)

        # Send a PUT request to the API
        response = requests.put(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def get_syscheck_results(self, agent_id: str, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list = None, q: str = None, distinct: bool = False, status: str = None, pci_dss: str = None, cis: str = None) -> dict:
        """
        Send a GET request to the syscheck API to retrieve the rootcheck database of an agent.

        Parameters:
        agent_id (str): The ID of the agent whose rootcheck database is to be retrieved.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): The first element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (list of str, optional): Select which fields to return. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.
        status (str, optional): Filter by status. Defaults to None.
        pci_dss (str, optional): Filter by PCI_DSS requirement name. Defaults to None.
        cis (str, optional): Filter by CIS requirement. Defaults to None.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/syscheck/{agent_id}"
    
        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "offset": offset,
        "limit": limit,
        "sort": sort,
        "search": search,
        "select": ",".join(select) if select else None,
        "q": q,
        "distinct": str(distinct).lower(),
        "status": status,
        "pci_dss": pci_dss,
        "cis": cis
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def clear_sysresults(self, pretty: bool = False, wait_for_complete: bool = False, agent_id = str >= 3) -> dict:
        """
        Send a PUT request to the sysresults api to run a rootcheck scan.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        agents_list (list of str, optional): List of agent IDs to target the scan. Defaults to None (run on all agents).

        Returns:
        dict: The API response as a dictionary.
        """
        
        # Validate agent_id length
        if len(agent_id) < 3:
            raise ValueError("Agent ID must be at least 3 characters long.")

        # Define the endpoint URL
        endpoint = f"{self.api_url}/syscheck/{agent_id}"
    
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

        # Send a Delete request to the API
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def get_last_sysscan(self, pretty: bool = False, wait_for_complete: bool = False, agent_id = str >= 3) -> dict:
        """
        Send a PUT request to the Syscheck API to run a rootcheck scan.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        agents_list (list of str, optional): List of agent IDs to target the scan. Defaults to None (run on all agents).

        Returns:
        dict: The API response as a dictionary.
        """
        
        # Validate agent_id length
        if len(agent_id) < 3:
            raise ValueError("Agent ID must be at least 3 characters long.")

        # Define the endpoint URL
        endpoint = f"{self.api_url}/syscheck/{agent_id}"
    
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

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()