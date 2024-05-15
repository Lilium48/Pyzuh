import requests 
from errors import handle_errors

class Groups: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def delete_groups(self, pretty: bool = False, wait_for_complete: bool = False, groups_list: list = None) -> dict:
        """
        Delete all groups or a list of them.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        groups_list (list, required): List of group names to delete, use 'all' to select all groups.

        Returns:
        dict: The response from the server after deleting the groups.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups"

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

        # Send a Delete request to the endpoint with the events as a JSON payload
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def get_groups(self, pretty: bool = False, wait_for_complete: bool = False, groups_list: list = None,
               offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
               hash_algorithm: str = None, q: str = None, select: list = None, distinct: bool = False) -> dict:
        """
        Retrieve information about all groups or a list of them. Returns a list containing basic information
        about each group, such as the number of agents belonging to the group and the checksums of the configuration
        and shared files.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        groups_list (list, optional): List of group IDs to filter results by. All groups selected by default
                                      if not specified. Defaults to None.
        offset (int, optional): The first element to return in the collection. Must be >= 0. Defaults to 0.
        limit (int, optional): The maximum number of elements to return. Defaults to 500. Up to 100,000 can be specified,
                              but it is recommended not to exceed 500 elements for optimal response time.
        sort (str, optional): Criteria for sorting the results. Use +/- at the beginning to specify ascending/descending order.
                             Use '.' for nested fields. Defaults to None.
        search (str, optional): Search string to filter results by. Use '-' at the beginning for complementary search. Defaults to None.
        hash_algorithm (str, optional): Hash algorithm to generate the returned checksums. Options include "md5", "sha1",
                                        "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256",
                                        "sha3_384", "sha3_512". Defaults to None.
        q (str, optional): Query string to filter results by. For example, q="status=active". Defaults to None.
        select (list, optional): List of fields to return. Use ',' to separate fields. Use '.' for nested fields. Defaults to None.
        distinct (bool, optional): Whether to return distinct values. Defaults to False.

        Returns:
        dict: Dictionary containing information about the specified groups.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "groups_list": ",".join(groups_list) if groups_list else None,
        "offset": offset,
        "limit": limit,
        "sort": sort,
        "search": search,
        "hash": hash_algorithm,
        "q": q,
        "select": ",".join(select) if select else None,
        "distinct": str(distinct).lower()
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def create_group(self, group_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Create a new group.

        Parameters:
        group_id (str): The name of the group to be created. It can contain any of the characters between
                        a-z, A-Z, 0-9, '_', '-' and '.'. Names '.' and '..' are restricted. Maximum length
                        is 128 characters.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The response containing information about the created group.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups"

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

        # Prepare request body
        body = {
        "group_id": group_id
        }

        # Send a POST request to the API endpoint with the group_id in the request body
        response = requests.post(endpoint, headers=headers, params=params, json=body)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_agents_in_group(self, group_id: str, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0,
                        limit: int = 500, select: list = None, sort: str = None, search: str = None,
                        status: list = None, q: str = None, distinct: bool = False) -> dict:
        """
        Return the list of agents that belong to the specified group.

        Parameters:
        group_id (str): Required parameter. The group ID (name of the group).
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Must be >= 0. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500. 
            Although up to 100,000 can be specified, it is recommended not to exceed 500 elements.
        select (list, optional): Select which fields to return (as a list of strings). Use '.' for nested fields (e.g., 'field1.field2').
        sort (str, optional): Sort the collection by a field or fields (separated by commas). Use '+' or '-' at the beginning to indicate ascending or descending order. Use '.' for nested fields.
        search (str, optional): Look for elements containing the specified string. To obtain a complementary search, use '-' at the beginning.
        status (list, optional): Filter by agent status (as a list of strings). Use commas to specify multiple statuses. Defaults to None.
        q (str, optional): Query to filter results by. For example q="status=active".
        distinct (bool, optional): Whether to look for distinct values. Defaults to False.

        Returns:
        dict: A dictionary containing the list of agents that belong to the specified group.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups/{group_id}/agents"

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
        "select": ",".join(select) if select else None,
        "sort": sort,
        "search": search,
        "status": ",".join(status) if status else None,
        "q": q,
        "distinct": str(distinct).lower()
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_group_config(self, group_id: str, pretty: bool = False, wait_for_complete: bool = False, 
                            offset: int = 0, limit: int = 500) -> dict:
        """
        Return the group configuration defined in the agent.conf file.

        Parameters:
        group_id (str): Required parameter. The group ID (name of the group).
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Must be >= 0. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500. 
            Although up to 100,000 can be specified, it is recommended not to exceed 500 elements. 
            Responses may be slower the more this number is exceeded.

        Returns:
        dict: A dictionary containing the group configuration as defined in the agent.conf file.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups/{group_id}/configuration"

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
        "limit": str(limit)
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def update_group_config(self, group_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Updates a specific group's configuration. Expects XML file with config tags and syntax. 

        Parameters:
        group_id (str): Required parameter. The group ID (name of the group).
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        Returns:
        dict: A dictionary containing the group configuration as defined in the agent.conf file.
        """

        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups/{group_id}/configuration"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/xml"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a PUT request to the endpoint
        response = requests.put(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_group_files(self, group_id: str, pretty: bool = False, wait_for_complete: bool = False,
               offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
               hash_algorithm: str = None, q: str = None, select: list = None, distinct: bool = False) -> dict:
        """
        Return the list of agents that belong to the specified group.
        Parameters:
        group_id (str): Required parameter. The group ID (name of the group).
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        groups_list (list, optional): List of group IDs to filter results by. All groups selected by default
                                      if not specified. Defaults to None.
        offset (int, optional): The first element to return in the collection. Must be >= 0. Defaults to 0.
        limit (int, optional): The maximum number of elements to return. Defaults to 500. Up to 100,000 can be specified,
                              but it is recommended not to exceed 500 elements for optimal response time.
        sort (str, optional): Criteria for sorting the results. Use +/- at the beginning to specify ascending/descending order.
                             Use '.' for nested fields. Defaults to None.
        search (str, optional): Search string to filter results by. Use '-' at the beginning for complementary search. Defaults to None.
        hash_algorithm (str, optional): Hash algorithm to generate the returned checksums. Options include "md5", "sha1",
                                        "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256",
                                        "sha3_384", "sha3_512". Defaults to None.
        q (str, optional): Query string to filter results by. For example, q="status=active". Defaults to None.
        select (list, optional): List of fields to return. Use ',' to separate fields. Use '.' for nested fields. Defaults to None.
        distinct (bool, optional): Whether to return distinct values. Defaults to False.

        Returns:
        dict: Dictionary containing information about the specified groups.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups/{group_id}/files"

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
        "select": ",".join(select) if select else None,
        "sort": sort,
        "search": search,
        "hash": hash_algorithm,
        "q": q,
        "distinct": str(distinct).lower()
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_group_file(self, group_id: str, file_name: str, type: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the contents of the specified group file parsed to XML.

        Parameters:
        group_id (str): Required parameter. The group ID (name of the group).
        file_name (str): Required parameter. The filename of the file to retrieve.
        type (str): Required parameter. The type of file. Must be one of "conf", "rootkit_files", "rootkit_trojans", "rcl".
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the contents of the specified group file parsed to XML.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups/{group_id}/{file_name}/xml"

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
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

    def get_group_file_json(self, group_id: str, file_name: str, file_type: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the content of the specified group file parsed to JSON.

        Parameters:
        group_id (str): Required parameter. The group ID (name of the group).
        file_name (str): Required parameter. The filename of the file to retrieve.
        file_type (str): Required parameter. The type of file. Must be one of "conf", "rootkit_files", "rootkit_trojans", or "rcl".
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the content of the specified group file parsed to JSON.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/groups/{group_id}/{file_name}/json"

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
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
