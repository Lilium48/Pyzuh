import requests 
from errors import handle_errors

class Security: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def logout_user(self) -> dict:
        """
        Invalidate all the current user's tokens by calling the logout API.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/user/authenticate"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Send a DELETE request to the API
        response = requests.delete(endpoint, headers=headers)

        # Parse and return the JSON response
        return response.json()
    
    def login_auth_context(self, raw: bool = False) -> dict:
        """
        Invalidate all the current user's tokens by calling the logout API.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/user/authenticate/run_as"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        params = {
            "raw":str(raw).lower()
        }
        # Send a post request to the API
        response = requests.post(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def get_current_user(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Get information of the current user. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The response from the server after ingesting the events.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/users/me"

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
        response = requests.post(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_current_user_policies(self, pretty: bool = False) -> dict:
        """
        Get processed policies info for the current user. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        Returns:
        dict: The response from the server after ingesting the events.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/users/me/policies"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
            }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        }

        # Send a POST request to the endpoint with the events as a JSON payload
        response = requests.post(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def revoke_jwt_tokens(self) -> dict:
        """
        Invalidate all current user tokens. 

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/user/authenticate"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }
        # Send a delete request to the API
        response = requests.delete(endpoint, headers=headers)

        # Parse and return the JSON response
        return response.json()
    def modify_run_as_flag(self, user_id: str, allow_run_as: bool, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Modify a user's allow_run_as flag by specifying their ID.

        Parameters:
        user_id (str): The user's ID.
        allow_run_as (bool): The value for the allow_run_as flag.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/user_management/{user_id}"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "allow_run_as": str(allow_run_as).lower(),
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a PUT request to the API
        response = requests.put(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def list_RBAC_actions(self, endpoint: str, pretty: bool = False) -> dict:
        """
        Modify a user's allow_run_as flag by specifying their ID.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        endpoint (str): Look for the RBAC actions which are related to the specified endpoints. 
        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/actions"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "endpoint": str(endpoint).lower
        }

        # Send a PUT request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def list_rbac_resources(self, resource: str = None, pretty: bool = False) -> dict:
        """
        Get all current defined RBAC resources.

        Parameters:
        resource (str, optional): List of current RBAC's resources. Enum: "*:*", "agent:group", "agent:id", "group:id", "node:id", "decoder:file", "list:file", "rule:file", "policy:id", "role:id", "user:id".
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/resources"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "resource": resource,
            "pretty": str(pretty).lower()
        }

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def list_users(self, user_ids: list = None, limit: int = 500, offset: int = 0, pretty: bool = False, search: str = None, select: list = None, sort: str = None, wait_for_complete: bool = False, q: str = None, distinct: bool = False) -> dict:
        """
        Get the information of specified users.

        Parameters:
        user_ids (list, optional): List of user IDs.
        limit (int, optional): Maximum number of elements to return.
        offset (int, optional): First element to return in the collection.
        pretty (bool, optional): Whether to return the response in a human-readable format.
        search (str, optional): Look for elements containing the specified string.
        select (list, optional): Select which fields to return.
        sort (str, optional): Sort the collection by a field or fields.
        wait_for_complete (bool, optional): Whether to disable timeout response.
        q (str, optional): Query to filter results by.
        distinct (bool, optional): Look for distinct values.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/users"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "user_ids": ','.join(user_ids) if user_ids else None,
            "limit": limit,
            "offset": offset,
            "pretty": str(pretty).lower(),
            "search": search,
            "select": ','.join(select) if select else None,
            "sort": sort,
            "wait_for_complete": str(wait_for_complete).lower(),
            "q": q,
            "distinct": str(distinct).lower()
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def add_user(self, username: str, password: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Add a new API user to the system.

        Parameters:
        username (str): The username of the new user.
        password (str): The password of the new user.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/users"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Create the request body
        request_body = {
            "username": username,
            "password": password
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

    def delete_users(self, user_ids: str, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Delete a user by specify the ID. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        user_ids(bool, required): List of User IDs. 
        
        Returns:
        dict: The API response as a dictionary.
        """
        
         # Ensure user_ids is not empty
        if not user_ids:
            raise ValueError("user_ids cannot be empty")
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/users"

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

        # Send a delete request to the endpoint with the request body
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def update_users(self, password: str, user_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Delete a user by specify the ID. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        user_ids(bool, required): List of User IDs. 
        
        Returns:
        dict: The API response as a dictionary.
        """
        
         # Ensure user_ids is not empty
        if not user_id:
            raise ValueError("user_ids cannot be empty")
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/users/{user_id}"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
            }
        
        body = { 
            "password": password
            }
        
        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a delete request to the endpoint with the request body
        response = requests.delete(endpoint, headers=headers, body=body, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def list_roles(self, user_ids: list = None, limit: int = 500, offset: int = 0, pretty: bool = False, search: str = None, select: list = None, sort: str = None, wait_for_complete: bool = False, q: str = None, distinct: bool = False) -> dict:
        """
        List the id separated by commas. 

        Parameters:
        role_ids (list, optional): List of user IDs.
        limit (int, optional): Maximum number of elements to return.
        offset (int, optional): First element to return in the collection.
        pretty (bool, optional): Whether to return the response in a human-readable format.
        search (str, optional): Look for elements containing the specified string.
        select (list, optional): Select which fields to return.
        sort (str, optional): Sort the collection by a field or fields.
        wait_for_complete (bool, optional): Whether to disable timeout response.
        q (str, optional): Query to filter results by.
        distinct (bool, optional): Look for distinct values.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/roles"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "user_ids": ','.join(user_ids) if user_ids else None,
            "limit": limit,
            "offset": offset,
            "pretty": str(pretty).lower(),
            "search": search,
            "select": ','.join(select) if select else None,
            "sort": sort,
            "wait_for_complete": str(wait_for_complete).lower(),
            "q": q,
            "distinct": str(distinct).lower()
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def add_roles(self, name: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Add a mew role with all fields need to be specified. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format.
        wait_for_complete (bool, optional): Whether to disable timeout response.
        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/roles"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "name": name
        }

        #Post Request
        response = requests.post(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def delete_roles(self, role_ids: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Deletes Roles. Policies linked to roles are not going to be removed. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format.
        wait_for_complete (bool, optional): Whether to disable timeout response.
        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/roles"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "role_ids": role_ids
        }

        #Delete Request
        response = requests.delete(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def update_roles(self, role_id: str, name: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Deletes Roles. Policies linked to roles are not going to be removed. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format.
        wait_for_complete (bool, optional): Whether to disable timeout response.
        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/roles"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "role_id": role_id
        }

        body = { 
            "name": name
            }
        
        #Put Request
        response = requests.put(endpoint, headers=headers, body=body, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def list_security_rules(self, rule_ids: list = None, limit: int = 500, offset: int = 0, pretty: bool = False, search: str = None, select: list = None, sort: str = None, wait_for_complete: bool = False, q: str = None, distinct: bool = False) -> dict:
        """
        Get a list of security rules from the system OR all of them. Must be mapped with roles to obtain certain access privileges. 

        Parameters:
        role_ids (list, optional): List of user IDs.
        limit (int, optional): Maximum number of elements to return.
        offset (int, optional): First element to return in the collection.
        pretty (bool, optional): Whether to return the response in a human-readable format.
        search (str, optional): Look for elements containing the specified string.
        select (list, optional): Select which fields to return.
        sort (str, optional): Sort the collection by a field or fields.
        wait_for_complete (bool, optional): Whether to disable timeout response.
        q (str, optional): Query to filter results by.
        distinct (bool, optional): Look for distinct values.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/rules"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "rule_ids": ','.join(rule_ids) if rule_ids else None,
            "limit": limit,
            "offset": offset,
            "pretty": str(pretty).lower(),
            "search": search,
            "select": ','.join(select) if select else None,
            "sort": sort,
            "wait_for_complete": str(wait_for_complete).lower(),
            "q": q,
            "distinct": str(distinct).lower()
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def add_security_rule(self, name: str, rule: dict, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Add a new security rule.

        Parameters:
        - name (str): Rule name.
        - rule (dict): Rule body.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/rules"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        }

        body = { 
        "name": name, 
        "rule": rule
        }
    
        # Post request
        response = requests.post(endpoint, headers=headers, json=body, params=params)

        # Parse and return the JSON response
        return response.json()

    def delete_security_rule(self, rule_ids: str, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Delete a new security rule. Roles linked to rules are not going to be deleted. 

        Parameters:
        - name (str): Rule name.
        - rule (dict): Rule body.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/rules"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "rule_ids": ','.join(rule_ids) if rule_ids else None
        }
        
         # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}
        
        #Delete request
        response = requests.delete(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()

    def update_security_rule(self, rule_id: str, name: str, rule: dict, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Modify a security rule by specifying its ID.

        Parameters:
        - rule_id (str): The ID of the security rule.
        - name (str): Rule name.
        - rule (dict): Rule body.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Check if name is longer than 64 characters
        if len(name) > 64:
            raise ValueError("Name must be less than or equal to 64 characters")

        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/rules/{rule_id}"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
        }

        body = { 
        "name": name,
        "rule": rule
        }

        # PUT request
        response = requests.put(endpoint, headers=headers, json=body, params=params)

        # Parse and return the JSON response
        return response.json()

    def list_policies(self, rule_ids: list = None, limit: int = 500, offset: int = 0, pretty: bool = False, search: str = None, select: list = None, sort: str = None, wait_for_complete: bool = False, q: str = None, distinct: bool = False) -> dict:
        """
        Get all policies in the system, including admin policy. 

        Parameters:
        role_ids (list, optional): List of user IDs.
        limit (int, optional): Maximum number of elements to return.
        offset (int, optional): First element to return in the collection.
        pretty (bool, optional): Whether to return the response in a human-readable format.
        search (str, optional): Look for elements containing the specified string.
        select (list, optional): Select which fields to return.
        sort (str, optional): Sort the collection by a field or fields.
        wait_for_complete (bool, optional): Whether to disable timeout response.
        q (str, optional): Query to filter results by.
        distinct (bool, optional): Look for distinct values.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/policies"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "rule_ids": ','.join(rule_ids) if rule_ids else None,
            "limit": limit,
            "offset": offset,
            "pretty": str(pretty).lower(),
            "search": search,
            "select": ','.join(select) if select else None,
            "sort": sort,
            "wait_for_complete": str(wait_for_complete).lower(),
            "q": q,
            "distinct": str(distinct).lower()
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def add_policy(self, name: str, rule: dict, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Add a new policy rule.

        Parameters:
        - name (str): Rule name.
        - rule (dict): Rule body.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/policies"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        }

        body = { 
        "name": name, 
        "rule": rule
        }
    
        # Post request
        response = requests.post(endpoint, headers=headers, json=body, params=params)

        # Parse and return the JSON response
        return response.json()

    def delete_policy(self, policy_ids: str, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Delete a new security rule. Roles linked to rules are not going to be deleted. 

        Parameters:
        - name (str): Rule name.
        - rule (dict): Rule body.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/policies"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "policy_ids": ','.join(policy_ids) if policy_ids else None
        }
        
         # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}
        
        #Delete request
        response = requests.delete(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()

    def update_policy(self, policy_id: str, name: str, policy: dict, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Modify a policy. 

        Parameters:
        - rule_id (str): The ID of the security rule.
        - name (str): Rule name.
        - rule (dict): Rule body.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Check if name is longer than 64 characters
        if len(name) > 64:
            raise ValueError("Name must be less than or equal to 64 characters")

        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/policies/{policy_id}"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
        }

        body = { 
        "name": name,
        "policy": policy
        }

        # PUT request
        response = requests.put(endpoint, headers=headers, json=body, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def add_roles_to_user(self, user_id: str, position: int, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Add a new policy rule.

        Parameters:
        - name (str): Rule name.
        - rule (dict): Rule body.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/users/{user_id}/roles"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "position": int(position)
        }
    
        # Post request
        response = requests.post(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def remove_roles_from_user(self, user_id: str, role_ids: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Remove roles from a user.

        Parameters:
        - user_id (str): User ID.
        - role_ids (str): List of Role IDs to remove. Use 'all' to select all roles.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/users/{user_id}/roles"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "role_ids": role_ids 
        }
    
        # Delete request
        response = requests.delete(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()

    def add_policies_to_role(self, role_id: str, policy_ids: str, position: int, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Remove roles from a user.

        Parameters:
        - user_id (str): User ID.
        - role_ids (str): List of Role IDs to remove. Use 'all' to select all roles.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/roles/{role_id}/policies"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "policy_ids": policy_ids, 
            "position": int(position)
        }
    
        # Post request
        response = requests.post(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def remove_policies_from_role(self, role_id: str, policy_ids: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Remove policies from role.

        Parameters:
        - user_id (str): User ID.
        - role_ids (str): List of Role IDs to remove. Use 'all' to select all roles.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/roles/{role_id}/policies"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "policy_ids": policy_ids 
        }
    
        # Delete request
        response = requests.delete(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def add_securityrule_to_role(self, role_id: str, rule_ids: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Add security role-rule situation. 1 to many concept. 

        Parameters:
        - user_id (str): User ID.
        - role_ids (str): List of Role IDs to remove. Use 'all' to select all roles.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/roles/{role_id}/rules"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "rule_ids": rule_ids, 
        }
    
        # Post request
        response = requests.post(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def remove_securityrule_to_role(self, role_id: str, rule_ids: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Remove security role-rule situation. 

        Parameters:
        - user_id (str): User ID.
        - role_ids (str): List of Role IDs to remove. Use 'all' to select all roles.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
    
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/roles/{role_id}/rules"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "rule_ids": rule_ids, 
        }
    
        #Delete request
        response = requests.delete(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def get_security_config(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the security config in json format. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The response from the server after ingesting the events.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/config"

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
        response = requests.post(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def update_security_config(self, auth_token_exp_timeout: int, rbac_mode: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Update the security configuration with the provided data.

        Parameters:
        - auth_token_exp_timeout (int): Time in seconds until the token expires. Must be >= 30.
        - rbac_mode (str): RBAC mode. Should be one of: "white" or "black".
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """

        # Validate auth_token_exp_timeout
        if auth_token_exp_timeout < 30:
            raise ValueError("auth_token_exp_timeout must be greater than or equal to 30.")

        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/config"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        }

        body = {
        "auth_token_exp_timeout": auth_token_exp_timeout,
        "rbac_mode": rbac_mode
        }

        # PUT request
        response = requests.put(endpoint, headers=headers, json=body, params=params)

        # Parse and return the JSON response
        return response.json()

    def restore_default_security_config(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the security config in json format. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The response from the server after ingesting the events.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/security/config"

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
        response = requests.put(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()