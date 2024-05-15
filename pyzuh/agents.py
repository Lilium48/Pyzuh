import requests
import json

from errors import handle_errors

class Agents: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def delete_agents(self, agents_list: str, status: list, pretty: bool = False, wait_for_complete: bool = False, purge: bool = False, older_than: str = "7d", q: str = "", os_platform: str = "", os_version: str = "", os_name: str = "", manager: str = "", version: str = "", group: str = "", node_name: str = "", name: str = "", ip: str = "", register_ip: str = "") -> dict:
        """
        Delete all agents or a list of them based on optional criteria.

        Parameters:
        - agents_list (str): List of agent IDs (separated by comma), use the keyword 'all' to select all agents.
        - status (list of str): Filter by agent status. Valid options: "all", "active", "pending", "never_connected", "disconnected".
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - purge (bool, optional): Permanently delete an agent from the key store. Defaults to False.
        - older_than (str, optional): Consider only agents whose last keep alive is older than the specified time frame. Defaults to "7d".
        - q (str, optional): Query to filter results by.
        - os_platform (str, optional): Filter by OS platform.
        - os_version (str, optional): Filter by OS version.
        - os_name (str, optional): Filter by OS name.
        - manager (str, optional): Filter by manager hostname where agents are connected to.
        - version (str, optional): Filter by agents version.
        - group (str, optional): Filter by group of agents.
        - node_name (str, optional): Filter by node name.
        - name (str, optional): Filter by name.
        - ip (str, optional): Filter by the IP used by the agent to communicate with the manager.
        - register_ip (str, optional): Filter by the IP used when registering the agent.

        Returns:
        dict: The API response as a dictionary.
        """

        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "purge": str(purge).lower(),
        "older_than": older_than,
        "q": q,
        "os.platform": os_platform,
        "os.version": os_version,
        "os.name": os_name,
        "manager": manager,
        "version": version,
        "group": group,
        "node_name": node_name,
        "name": name,
        "ip": ip,
        "registerIP": register_ip
        }

        body = {
        "agents_list": agents_list.split(','),
        "status": status
        }

        # Send a delete request to the endpoint with the request body
        response = requests.delete(endpoint, headers=headers, json=body, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def list_agents(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: str = "", offset: int = 0, limit: int = 500, select: list = [], sort: str = "", search: str = "", status: list = [], q: str = "", older_than: str = "", os_platform: str = "", os_version: str = "", os_name: str = "", manager: str = "", version: str = "", group: str = "", node_name: str = "", name: str = "", ip: str = "", register_ip: str = "", group_config_status: str = "", distinct: bool = False) -> dict:
        """
        Return information about all available agents or a list of them.

        Parameters:
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - agents_list (str, optional): List of agent IDs (separated by comma), all agents selected by default if not specified.
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500. Maximum value is 100000, but it's recommended not to exceed 500.
        - select (list of str, optional): Select which fields to return (separated by comma).
        - sort (str, optional): Sort the collection by a field or fields (separated by comma).
        - search (str, optional): Look for elements containing the specified string.
        - status (list of str, optional): Filter by agent status.
        - q (str, optional): Query to filter results by.
        - older_than (str, optional): Filter out agents whose time lapse from last keep alive signal is longer than specified.
        - os_platform (str, optional): Filter by OS platform.
        - os_version (str, optional): Filter by OS version.
        - os_name (str, optional): Filter by OS name.
        - manager (str, optional): Filter by manager hostname where agents are connected to.
        - version (str, optional): Filter by agents version.
        - group (str, optional): Filter by group of agents.
        - node_name (str, optional): Filter by node name.
        - name (str, optional): Filter by name.
        - ip (str, optional): Filter by the IP used by the agent to communicate with the manager.
        - register_ip (str, optional): Filter by the IP used when registering the agent.
        - group_config_status (str, optional): Agent groups configuration sync status.
        - distinct (bool, optional): Look for distinct values.

        Returns:
        dict: The API response as a dictionary.
        """

        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents"

        # Create headers for the API request
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
            }   

        # Prepare query parameters and body
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": agents_list,
        "offset": offset,
        "limit": limit,
        "select": ','.join(select),
        "sort": sort,
        "search": search,
        "status": ','.join(status),
        "q": q,
        "older_than": older_than,
        "os.platform": os_platform,
        "os.version": os_version,
        "os.name": os_name,
        "manager": manager,
        "version": version,
        "group": group,
        "node_name": node_name,
        "name": name,
        "ip": ip,
        "registerIP": register_ip,
        "group_config_status": group_config_status,
        "distinct": str(distinct).lower()
        }

        # Send a GET request to the endpoint with the query parameters
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
    
    def add_agent(self, name: str, ip: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Add a new Agent. 

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
            "name": name,
            "ip": ip
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
    
    def get_active_configuration(self, agent_id: str, component: str, configuration: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the active configuration the agent is currently using.

         Parameters:
        - agent_id (str): Agent ID. Must be at least 3 characters long.
        - component (str): Selected agent's component. Options: "agent", "agentless", "analysis", "auth", "com", "csyslog", "integrator", "logcollector", "mail", "monitor", "request", "syscheck", "wazuh-db", "wmodules".
        - configuration (str): Selected agent's configuration to read. The configuration to read depends on the selected component.

        Returns:
        dict: The active configuration as a dictionary.
        """

        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/{agent_id}/config/{component}/{configuration}"

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

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def remove_agent_from_group(self, agent_id: str, pretty: bool = False, wait_for_complete: bool = False, groups_list: list = None) -> dict:
        """
        Send a PUT request to the run scan API to run a rootcheck scan.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        agents_list (list of str, optional): List of agent IDs to target the scan. Defaults to None (run on all agents).

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agent/{agent_id}/group"
    
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
        if groups_list:
            params["groups_list"] = ",".join(groups_list)

        # Send a Delete request to the API
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def remove_agent_from_group(self, agent_id: str, group_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Remove an agent from a specified group.

        Parameters:
        - agent_id (str): Agent ID. Must be at least 3 characters long.
        - group_id (str): Group ID. Name of the group.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/{agent_id}/group/{group_id}"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a DELETE request to the API
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def assign_agent_to_group(self, agent_id: str, group_id: str, force_single_group: bool, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Assign an agent to a specified group.

        Parameters:
        - agent_id (str): Agent ID. Must be at least 3 characters long.
        - group_id (str): Group ID. Name of the group.
        - force_single_group (bool): Whether to remove the agent from all groups to which it belongs and assign it to the specified group.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/{agent_id}/group/{group_id}"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "force_single_group": str(force_single_group).lower()
        }

        # Send a PUT request to the API
        response = requests.put(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def get_key(self, agent_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Assign an agent to a specified group.

        Parameters:
        - agent_id (str): Agent ID. Must be at least 3 characters long.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/{agent_id}/key"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def restart_agent(self, agent_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Assign an agent to a specified group.

        Parameters:
        - agent_id (str): Agent ID. Must be at least 3 characters long.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/{agent_id}/restart"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def get_wazuh_daemon_stats(self, agent_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Assign an agent to a specified group.

        Parameters:
        - agent_id (str): Agent ID. Must be at least 3 characters long.
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        - daemmons_list: string array, must enumerate "wazuh-analysisd" and "wazuh-remoted". All daemons selected by default. 
        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/{agent_id}/daemons/stats"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def get_component_stats(self, agent_id: str, component: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Get statistics for a selected component of an agent.

        Parameters:
        - agent_id (str): Agent ID. Must be at least 3 characters long.
        - component (str): Selected component stats. Options: "logcollector", "agent".
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agent/{agent_id}/component/{component}"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower()
        }

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()

    def upgrade_agents(self, agents_list: list[str], wpk_repo: str, upgrade_version: str, use_http: bool = False, force: bool = False, pretty: bool = False, wait_for_complete: bool = False, q: str = "", os_platform: str = "", os_version: str = "", os_name: str = "", manager: str = "", version: str = "", group: str = "", node_name: str = "", name: str = "", ip: str = "", register_ip: str = "") -> dict:
        """
        Upgrade agents using a WPK file from an online repository.

        Parameters:
        - agents_list (list of str): List of agent IDs to upgrade. Use the keyword "all" to select all agents.
        - wpk_repo (str): URL of the WPK repository.
        - upgrade_version (str): Version of Wazuh to upgrade to.
        - use_http (bool, optional): Use HTTP protocol instead of HTTPS. Default is False.
        - force (bool, optional): Force upgrade. Default is False.
        - pretty (bool, optional): Show results in human-readable format. Default is False.
        - wait_for_complete (bool, optional): Disable timeout response. Highly recommended when upgrading more than 3000 agents simultaneously. Default is False.
        - q (str, optional): Query to filter results by. For example, q="status=active".
        - os_platform (str, optional): Filter by OS platform.
        - os_version (str, optional): Filter by OS version.
        - os_name (str, optional): Filter by OS name.
        - manager (str, optional): Filter by manager hostname where agents are connected to.
        - version (str, optional): Filter by agents version using one of the following formats: 'X.Y.Z', 'vX.Y.Z', 'wazuh X.Y.Z', or 'wazuh vX.Y.Z'. For example: '4.4.0'.
        - group (str, optional): Filter by group of agents.
        - node_name (str, optional): Filter by node name.
        - name (str, optional): Filter by name.
        - ip (str, optional): Filter by the IP used by the agent to communicate with the manager. If not available, it will have the same value as registerIP.
        - register_ip (str, optional): Filter by the IP used when registering the agent.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/upgrade"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the payload
        params = {
        "agents_list": agents_list,
        "wpk_repo": wpk_repo,
        "upgrade_version": upgrade_version,
        "use_http": use_http,
        "force": force,
        "pretty": pretty,
        "wait_for_complete": wait_for_complete,
        "q": q,
        "os": {
            "platform": os_platform,
            "version": os_version,
            "name": os_name
        },
        "manager": manager,
        "version": version,
        "group": group,
        "node_name": node_name,
        "name": name,
        "ip": ip,
        "registerIP": register_ip
        }

        # Send a PUT request to the API
        response = requests.put(endpoint, params=params, headers=headers)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()
        
    def upgrade_agents_custom(self, agents_list: list[str], file_path: str, wait_for_complete: bool = False, pretty: bool = False, **kwargs):
        """
        Upgrade agents using a local WPK file.

        Parameters:
      - agents_list (list[str]): Required. List of agent IDs (separated by comma) or the keyword "all" to select all agents.
      - file_path (str): Required. Full path to the local WPK file on the Wazuh server (default installation directory: /var/ossec).
      - wait_for_complete (bool, optional): Default: False. Disable timeout response. Highly recommended when upgrading more than 3000 agents simultaneously.
      - pretty (bool, optional): Default: False. Show results in human-readable format.
      - **kwargs (optional): Additional filter parameters:
          - q (str): Query to filter results by. For example q="status=active".
          - os (dict, optional): Filter by operating system details:
              - platform (str): Filter by OS platform.
              - version (str): Filter by OS version.
              - name (str): Filter by OS name.
          - manager (str): Filter by manager hostname where agents are connected to.
          - version (str): Filter by agents version using one of the following formats: 'X.Y.Z', 'vX.Y.Z', 'wazuh X.Y.Z', or 'wazuh vX.Y.Z'. For example: '4.4.0'.
          - group (str): Filter by group of agents.
          - node_name (str): Filter by node name.
          - name (str): Filter by name.
          - ip (str): Filter by the IP used by the agent to communicate with the manager. If not available, it will have the same value as registerIP.
          - registerIP (str): Filter by the IP used when registering the agent.

        Returns:
      dict: The API response as a dictionary.
        """
        # Define the endpoint URL (might be different for WPK upgrade)
        endpoint = f"{self.api_url}/agents/upgrade_custom"  

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        #Param
        params = {
      "agents_list": agents_list,
      "file_path": file_path,
      "pretty": pretty,
      "wait_for_complete": wait_for_complete
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}


        # Send a POST request
        response = requests.post(endpoint, params=params, headers=headers)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def get_upgrade_results(self, agents_list: list[str] = None, pretty: bool = False, wait_for_complete: bool = False, q: str = None, 
            os_platform: str = None, os_version: str = None, os_name: str = None, manager: str = None, version: str = None, 
            group: str = None, node_name: str = None, name: str = None, ip: str = None, register_ip: str = None) -> dict:
        """
        Get the results of a previous agent upgrade.

        Parameters:
      - agents_list (list[str], optional): List of agent IDs (separated by comma) to retrieve results for. Defaults to all agents.
      - pretty (bool, optional): Default: False. Show results in human-readable format.
      - wait_for_complete (bool, optional): Default: False. Disable timeout response.
      - **kwargs (optional): Additional filter parameters:
          - q (str): Query to filter results by. For example q="status=active".
          - os (dict, optional): Filter by operating system details:
              - platform (str): Filter by OS platform.
              - version (str): Filter by OS version.
              - name (str): Filter by OS name.
          - manager (str): Filter by manager hostname where agents are connected to.
          - version (str): Filter by agents version using one of the following formats: 'X.Y.Z', 'vX.Y.Z', 'wazuh X.Y.Z', or 'wazuh vX.Y.Z'. For example: '4.4.0'.
          - group (str): Filter by group of agents.
          - node_name (str): Filter by node name.
          - name (str): Filter by name.
          - ip (str): Filter by the IP used by the agent to communicate with the manager. If not available, it will have the same value as registerIP.
          - registerIP (str): Filter by the IP used when registering the agent.

        Returns:
      dict: The API response as a dictionary containing the upgrade results.
        """

        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/upgrade_result"  

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the payload
        params = {
        "pretty": pretty,
        "wait_for_complete": wait_for_complete,
        "agents_list": agents_list,
        "q": q,
        "os": {
        "platform": os_platform,
        "version": os_version,
        "name": os_name
        },
        "manager": manager,
        "version": version,
        "group": group,
        "node_name": node_name,
        "name": name,
        "ip": ip,
        "registerIP": register_ip
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a get request
        response = requests.get(endpoint, params=params, headers=headers)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def restart_agents_in_group(self, group_id: str = "", pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Restart all agents which belong to a given group

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        group_id (str, optional): Group ID. (Name of the group). Defaults to "".

        Returns:
        dict: The response containing information about the sync status of specific nodes.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/group/{group_id}/restart"

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

        # Send a put request to the endpoint
        response = requests.put(endpoint, headers=headers, params=params)
    
        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()
    
    def add_agent_full(self, agent_id: str, agent_key: str, agent_name: str, agent_ip: str = None, force: bool = False, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Add an agent specifying its name, ID, and IP. If an agent with the same name, ID, or IP already exists, replace it using the force parameter.

        Parameters:
        agent_id (str): Agent ID. Must be at least 3 characters long.
        agent_key (str): Key to use when communicating with the manager. The agent must have the same key on its client.keys file.
        agent_name (str): Agent name.
        agent_ip (str, optional): Agent IP. If not included, the API will get the IP automatically. Allowed values: IP, IP/NET, ANY.
        force (bool, optional): Remove the old agent with the same name, ID, or IP if the configuration is matched. Defaults to False.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/insert"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "id": agent_id,
        "key": agent_key,
        "name": agent_name,
        "force": force
        }

        # Add agent IP to params if provided
        if agent_ip:
            params["ip"] = agent_ip

        # Send a POST request to the API
        response = requests.post(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()
    
    def add_agent_quick(self, agent_name: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Add a new agent with the specified name. This agent will use 'any' as the IP.

        Parameters:
        agent_name (str): Agent name. Allowed special characters: '-', '_', '.'. Max length: 128 characters.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The API response as a dictionary.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/insert/quick"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agent_name": agent_name
        }

        # Send a POST request to the API
        response = requests.post(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()
    
    def list_agents_without_group(self, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, select: list = None, sort: str = None, search: str = None, q: str = None) -> dict:
        """
        Return a list with all available agents without an assigned group.

        Parameters:
        pretty (bool, optional): Whether to show results in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        select (list of str, optional): Select which fields to return (separated by comma). Defaults to None.
        sort (str, optional): Sort the collection by a field or fields (separated by comma). Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.

        Returns:
        dict: The response containing the list of agents without a group.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/no_group"

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
        "limit": limit
        }

        # Add optional parameters
        if select:
            params['select'] = ','.join(select)
        if sort:
            params['sort'] = sort
        if search:
            params['search'] = search
        if q:
            params['q'] = q

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def restart_agents_in_node(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Restarts all agents which belong to a specific given node. 

        Parameters:
        node_id (str): Cluster node name.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The response containing information about the sync status of specific nodes.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/node/{node_id}/restart"

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

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
    
        # Handle errors in the response
        handle_errors(response)
    
        # Parse and return the JSON response
        return response.json()
    
    def list_outdated_agents(self, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, q: str = None) -> dict:
        """
        Return a list with all available agents without an assigned group.

        Parameters:
        pretty (bool, optional): Whether to show results in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields (separated by comma). Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.

        Returns:
        dict: The response containing the list of agents without a group.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/no_group"

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
        "search": search, 
        "q": q
        }

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def force_reconnect_agents(self, pretty: bool = False, agents_list: str = None, wait_for_complete: bool = False) -> dict:
        """
        Force reconnect all agents or a list of them

        Parameters:
            agents_list (str, optional): List of agent IDs, or use the keyword "all" to select all agents.
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
            dict: The response from the server.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/reconnect"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "agents_list": agents_list if agents_list == "all" else ",".join(agents_list) if agents_list else None
        }

        # Send a PUT request to the endpoint
        response = requests.put(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def restart_agents(self, pretty: bool = False, agents_list: str = None, wait_for_complete: bool = False) -> dict:
        """
        Force reconnect all agents or a list of them

        Parameters:
            agents_list (str, optional): List of agent IDs, or use the keyword "all" to select all agents.
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
            dict: The response from the server.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/restart"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "agents_list": agents_list if agents_list == "all" else ",".join(agents_list) if agents_list else None
        }

        # Send a PUT request to the endpoint
        response = requests.put(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def list_agents_distinct(self, fields: list, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, sort: str = None, search: str = None, q: str = None) -> dict:
        """
        Return all the different combinations that agents have for the selected fields, along with the total number of agents that have each combination.

        Parameters:
        fields (list of str): List of fields affecting the operation.
        pretty (bool, optional): Whether to show results in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields (separated by comma). Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.

        Returns:
        dict: The response containing the distinct combinations of agent fields.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/stats/distinct"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "fields": ','.join(fields),
        "offset": offset,
        "limit": limit,
        "sort": sort, 
        "search": search, 
        "q": q
        }

        # Send a GET request to the API
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def summarize_agents_OS(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return a summary of the OS of available agents. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The response from the server after ingesting the events.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/summary/os"

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
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def summarize_agents_status(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the security config in json format. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
        dict: The response from the server after ingesting the events.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/summary/status"

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
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()