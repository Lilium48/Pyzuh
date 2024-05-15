import requests
from errors import handle_errors

class Rules: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
        
    def list_rules(self, rule_ids: list[int] = None, pretty: bool = False, wait_for_complete: bool = False,
               offset: int = 0, limit: int = 500, select: list[str] = None, sort: str = None, search: str = None,
               q: str = None, status: str = None, group: str = None, level: str = None, filename: list[str] = None,
               relative_dirname: str = None, pci_dss: str = None, gdpr: str = None, gpg13: str = None,
               hipaa: str = None, nist_800_53: str = None, tsc: str = None, mitre: str = None,
               distinct: bool = False) -> dict:
        """
        List rules and their information from the Wazuh API.

        Parameters:
        - rule_ids (list[int], optional): List of rule IDs to filter by. Defaults to None.
        - pretty (bool, optional): Whether to show results in human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500.
        - select (list[str], optional): Fields to return (comma-separated). Defaults to None.
        - sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        - search (str, optional): Look for elements containing the specified string. Defaults to None.
        - q (str, optional): Query to filter results by. Defaults to None.
        - status (str, optional): Filter by list status. Defaults to None.
        - group (str, optional): Filter by rule group. Defaults to None.
        - level (str, optional): Filter by rule level. Defaults to None.
        - filename (list[str], optional): Filter by filename. Defaults to None.
        - relative_dirname (str, optional): Filter by relative directory name. Defaults to None.
        - pci_dss (str, optional): Filter by PCI_DSS requirement name. Defaults to None.
        - gdpr (str, optional): Filter by GDPR requirement. Defaults to None.
        - gpg13 (str, optional): Filter by GPG13 requirement. Defaults to None.
        - hipaa (str, optional): Filter by HIPAA requirement. Defaults to None.
        - nist_800_53 (str, optional): Filter by NIST-800-53 requirement. Defaults to None.
        - tsc (str, optional): Filter by TSC requirement. Defaults to None.
        - mitre (str, optional): Filter by MITRE technique ID. Defaults to None.
        - distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        - dict: A dictionary containing information about each rule.
        """
        #Define the endpoint URL
        endpoint = f"{self.api_url}/rules"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
        "rule_ids": rule_ids,
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "offset": offset,
        "limit": limit,
        "select": ','.join(select) if select else None,
        "sort": sort,
        "search": search,
        "q": q,
        "status": status,
        "group": group,
        "level": level,
        "filename": ','.join(filename) if filename else None,
        "relative_dirname": relative_dirname,
        "pci_dss": pci_dss,
        "gdpr": gdpr,
        "gpg13": gpg13,
        "hipaa": hipaa,
        "nist-800-53": nist_800_53,
        "tsc": tsc,
        "mitre": mitre,
        "distinct": str(distinct).lower()
        }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def get_groups(self, pretty: bool = False, wait_for_complete: bool = False,
               offset: int = 0, limit: int = 500, sort: str = None, search: str = None) -> dict:
        """
        List rules and their information from the Wazuh API.

        Parameters:
        - pretty (bool, optional): Whether to show results in human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500.
        - sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        - search (str, optional): Look for elements containing the specified string. Defaults to None.
        
        Returns:
        - dict: A dictionary containing information about each rule.
        """

        #Define the endpoint URL
        endpoint = f"{self.api_url}/rules/groups"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "offset": offset,
        "limit": limit,
        "sort": sort,
        "search": search
        } 
        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()

    def get_requirements(self, requirement: str, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None) -> dict:
        """
         Send a GET request to retrieve all specified requirement names defined in the Wazuh ruleset.

        Parameters:
        requirement (str): The specific requirement name to retrieve. Enum: "pci_dss", "gdpr", "hipaa", "nist-800-53", "gpg13", "tsc", "mitre".
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): The first element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.

        Returns:
        dict: The API response as a dictionary.
        """
       # Validate requirement parameter
        if requirement not in ("pci_dss", "gdpr", "hipaa", "nist-800-53", "gpg13", "tsc", "mitre"):
            raise ValueError("Invalid requirement. Allowed values are: pci_dss, gdpr, hipaa, nist-800-53, gpg13, tsc, mitre")
        
        #Define the endpoint URL
        endpoint = f"{self.api_url}/rules/requirement/{requirement}"

        # Create headers for the API request
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
        "search": search
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()
    
    def get_files(self, pretty: bool = False, wait_for_complete: bool = False,
               offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
               q: str = None, status: str = None, filename: list[str] = None,
               relative_dirname: str = None, distinct: bool = False) -> dict:
        """
        Gets Files from the Wazuh API. 

        Parameters:
        - pretty (bool, optional): Whether to show results in human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500.
        - select (list[str], optional): Fields to return (comma-separated). Defaults to None.
        - sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        - search (str, optional): Look for elements containing the specified string. Defaults to None.
        - q (str, optional): Query to filter results by. Defaults to None.
        - status (str, optional): Filter by list status. Defaults to None.
        - filename (list[str], optional): Filter by filename. Defaults to None.
        - relative_dirname (str, optional): Filter by relative directory name. Defaults to None.
        - distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        - dict: A dictionary containing information about each rule.
        """
        #Define the endpoint URL
        endpoint = f"{self.api_url}/rules/files"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "offset": offset,
        "limit": limit,
        "sort": sort,
        "search": search,
        "q": q,
        "status": status,
        "filename": ','.join(filename) if filename else None,
        "relative_dirname": relative_dirname,
        "distinct": str(distinct).lower()
        }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def get_rules_content(self, filename: str, pretty: bool = False, wait_for_complete: bool = False, raw: bool = False, relative_dirname: str = None) -> dict:
        """
        Return the content of a specified rule in the ruleset.

        Parameters:
        filename (str): The filename (rule or decoder) to download/upload/edit file.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        raw (bool, optional): Format response in plain text.
        relative_dirname (str, optional): Filter by relative directory name.

        Returns:
        dict: A dictionary containing the content of the specified rule.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/rules/files/{filename}"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "raw": str(raw).lower(),
            "relative_dirname": relative_dirname
        }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()
    
    def update_rules_file(self, filename: str, pretty: bool = False, wait_for_complete: bool = False, overwrite: bool = False, relative_dirname: str = None) -> dict:
        """
        Return the content of a specified rule in the ruleset.

        Parameters:
        filename (str): The filename (rule or decoder) to download/upload/edit file.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        overwrite (bool, optional): Exception raised when updating on existing filename. Defaults to False. 
        relative_dirname (str, optional): Filter by relative directory name.

        Returns:
        dict: A dictionary containing the content of the specified rule.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/rules/files/{filename}"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "overwrite": str(overwrite).lower(),
            "relative_dirname": relative_dirname
        }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a put request
        response = requests.put(endpoint, headers=headers, params=params)

        # Handle errors in the response
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()
    
    def delete_files_rule(self, filename: str, pretty: bool = False, wait_for_complete: bool = False, relative_dirname: str = None) -> dict:
        """
        Return the content of a specified rule in the ruleset.

        Parameters:
        filename (str): The filename (rule or decoder) to download/upload/edit file.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        relative_dirname (str, optional): Filter by relative directory name.

        Returns:
        dict: A dictionary containing the content of the specified rule.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/rules/files/{filename}"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "relative_dirname": relative_dirname
        }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}
        response = requests.delete(endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()