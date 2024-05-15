import requests
from errors import handle_errors

class Mitre: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def get_mitre_groups(self, group_ids: list[str] = None, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list[str] = None, q: str = None, distinct: bool = False) -> dict:
        """
        Retrieve MITRE groups from the MITRE database.

        Parameters:
        group_ids (List[str], optional): List of MITRE group IDs. Defaults to None.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (List[str], optional): Select which fields to return. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: A dictionary containing the response with MITRE groups.
        """
     # Define the endpoint URL
        endpoint = f"{self.api_url}/mitre/groups"

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
        "group_ids": ','.join(group_ids) if group_ids else None,
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "q": q,
        "distinct": str(distinct).lower(),
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_mitre_metadata(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Get Mitre Metadata. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/mitre/metadata"

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
    
    def get_mitre_mitigations(self, mitigation_ids: list[str] = None, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list[str] = None, q: str = None, distinct: bool = False) -> dict:
        """
        Retrieve MITRE mitigations from the MITRE database.

        Parameters:
        group_ids (List[str], optional): List of MITRE group IDs. Defaults to None.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (List[str], optional): Select which fields to return. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: A dictionary containing the response with MITRE groups.
        """
     # Define the endpoint URL
        endpoint = f"{self.api_url}/mitre/mitigations"

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
        "mitigation_ids": ','.join(mitigation_ids) if mitigation_ids else None,
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "q": q,
        "distinct": str(distinct).lower(),
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_mitre_references(self, reference_ids: list[str] = None, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list[str] = None, q: str = None, distinct: bool = False) -> dict:
        """
        Retrieve MITRE references from the MITRE database.

        Parameters:
        group_ids (List[str], optional): List of MITRE group IDs. Defaults to None.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (List[str], optional): Select which fields to return. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: A dictionary containing the response with MITRE groups.
        """
     # Define the endpoint URL
        endpoint = f"{self.api_url}/mitre/groups"

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
        "reference_ids": ','.join(reference_ids) if reference_ids else None,
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "q": q,
        "distinct": str(distinct).lower(),
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_mitre_software(self, software_ids: list[str] = None, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list[str] = None, q: str = None, distinct: bool = False) -> dict:
        """
        Retrieve MITRE software from the MITRE database.

        Parameters:
        group_ids (List[str], optional): List of MITRE group IDs. Defaults to None.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (List[str], optional): Select which fields to return. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: A dictionary containing the response with MITRE groups.
        """
     # Define the endpoint URL
        endpoint = f"{self.api_url}/mitre/software"

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
        "software_ids": ','.join(software_ids) if software_ids else None,
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "q": q,
        "distinct": str(distinct).lower(),
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_mitre_tactics(self, tactic_ids: list[str] = None, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list[str] = None, q: str = None, distinct: bool = False) -> dict:
        """
        Return Mitre Tactics from database. 

        Parameters:
        group_ids (List[str], optional): List of MITRE group IDs. Defaults to None.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (List[str], optional): Select which fields to return. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: A dictionary containing the response with MITRE groups.
        """
     # Define the endpoint URL
        endpoint = f"{self.api_url}/mitre/tactics"

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
        "tactic_ids": ','.join(tactic_ids) if tactic_ids else None,
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "q": q,
        "distinct": str(distinct).lower(),
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_mitre_techniques(self, technique_ids: list[str] = None, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, select: list[str] = None, q: str = None, distinct: bool = False) -> dict:
        """
        Return techniques from MITRE Database.

        Parameters:
        group_ids (List[str], optional): List of MITRE group IDs. Defaults to None.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        select (List[str], optional): Select which fields to return. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: A dictionary containing the response with MITRE groups.
        """
     # Define the endpoint URL
        endpoint = f"{self.api_url}/mitre/techniques"

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
        "technique_ids": ','.join(technique_ids) if technique_ids else None,
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "q": q,
        "distinct": str(distinct).lower(),
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()