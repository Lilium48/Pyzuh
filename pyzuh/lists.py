import requests
from errors import handle_errors

class Lists: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def get_cdb_lists(self, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, 
                limit: int = 500, select: list = None, sort: str = None, search: str = None, 
                relative_dirname: str = None, filename: list = None, q: str = None, distinct: bool = False) -> dict:
        """
        Returns the contents of all CDB lists. Optionally, the result can be filtered by several criteria. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
            offset (int, optional): First element to return in the collection. Defaults to 0.
            limit (int, optional): Maximum number of elements to return. Defaults to 500.
            select (list, optional): List of fields to return, specified as field names. Defaults to None.
            sort (str, optional): Criteria for sorting the results. Defaults to None.
            search (str, optional): Search string for filtering results. Defaults to None.
            relative_dirname (str, optional): Filter results by relative directory name. Defaults to None.
            filename (list, optional): Filter results by filename, specified as a list of strings. Defaults to None.
            q (str, optional): Query string to filter results by. Defaults to None.
            distinct (bool, optional): Look for distinct values. Defaults to False.
            
        Returns:
            dict: The response containing information about CDB Lists.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/lists"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare the params dictionary
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "offset": offset,
            "limit": limit,
            "select": ",".join(select) if select else None,
            "sort": sort,
            "search": search,
            "relative_dirname": relative_dirname,
            "filename": ",".join(filename) if filename else None,
            "q": q,
            "distinct": str(distinct).lower()
            }
        # Remove None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Make the GET request
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_cdb_list_file_content(self, filename: str, pretty: bool = False, wait_for_complete: bool = False, raw: bool = False) -> dict:
        """
        Return the content of a CDB list file.

        Parameters:
        filename (str): Required parameter. Filename (CDB list) to get/edit/delete.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        raw (bool, optional): Whether to format the response in plain text. Defaults to False.

        Returns:
        dict: A dictionary containing the content of the specified CDB list file.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/lists/files/{filename}"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "raw": str(raw).lower()
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def update_cdb_list_file_content(self, filename: str, pretty: bool = False, wait_for_complete: bool = False, overwrite: bool = False) -> dict:
        """
        Updates the content of a CDB list file.

        Parameters:
        filename (str): Required parameter. Filename (CDB list) to get/edit/delete.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        overwrite (bool, optional): Whether to format the response in plain text. Defaults to False.

        Returns:
        dict: A dictionary containing the content of the specified CDB list file.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/lists/files/{filename}"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "overwrite": str(overwrite).lower()
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.put(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def delete_cdb_list_file(self, filename: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Deletes a cdb list file. 

        Parameters:
        filename (str): Required parameter. Filename (CDB list) to get/edit/delete.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        overwrite (bool, optional): Whether to format the response in plain text. Defaults to False.

        Returns:
        dict: A dictionary containing the content of the specified CDB list file.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/lists/files/{filename}"

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

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_cdb_lists_files(self, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, relative_dirname: str = None, filename: list = None) -> dict:
        """
        Retrieve the path of all CDB lists.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        offset (int, optional): The first element to return in the collection. Defaults to 0.
        limit (int, optional): The maximum number of elements to return. Defaults to 500.
        sort (str, optional): Field(s) to sort the collection by. Defaults to None.
        search (str, optional): String to search for in the collection. Defaults to None.
        relative_dirname (str, optional): Filter by relative directory name. Defaults to None.
        filename (list, optional): Filter by filename. Defaults to None.

        Returns:
        dict: A dictionary containing information about the CDB lists.
        """

        # Define the endpoint URL
        endpoint = f"{self.api_url}/list/files"

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
        "relative_dirname": relative_dirname,
        "filename": ",".join(filename) if filename else None
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
