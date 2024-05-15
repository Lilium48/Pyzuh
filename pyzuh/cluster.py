import requests
from errors import handle_errors

class Cluster:
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def get_local_node(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Retrieve basic information about the local cluster node.

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
            dict: The response containing local node information.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/local/info"

        # Create headers using the JWT token
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
    
    def get_nodes_info(self, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, 
                      limit: int = 500, select: list = None, sort: str = None, search: str = None, 
                      relative_dirname: str = None, filename: list = None, q: str = None, distinct: bool = False, 
                      nodes_list: list = None) -> dict:
        """
        Retrieve information about cluster nodes based on specified filters.

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
            nodes_list (list, optional): List of node IDs to filter results for (separated by commas). Defaults to None.

        Returns:
            dict: The response containing information about cluster nodes based on the provided filters.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/nodes"

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
            "distinct": str(distinct).lower(),
            "nodes_list": ",".join(nodes_list) if nodes_list else None
        }

        # Remove None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Make the GET request
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def get_node_healthcheck(self, pretty: bool = False, wait_for_complete: bool = False, nodes_list: list = None) -> dict:
        """
        Retrieve the healthcheck of the local cluster nodes.

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
            nodes_list (list, optional): List of node IDs to filter results for (separated by commas). Defaults to None.

        Returns:
            dict: The response containing information about the health of the specified nodes.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/healthcheck"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "nodes_list": ",".join(nodes_list) if nodes_list else None
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()

    def get_node_syncstatus(self, pretty: bool = False, wait_for_complete: bool = False, nodes_list: list = None) -> dict:
        """
        Retrieve the Sync status of the local cluster nodes. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
            nodes_list (list, optional): List of node IDs to filter results for (separated by commas). Defaults to None.

        Returns:
            dict: The response containing information about the sync status of specific nodes.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/ruleset/synchronization"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "nodes_list": ",".join(nodes_list) if nodes_list else None
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_cluster_status(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Retrieve the status of the cluster. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
            dict: The response containing information about the health of the specified nodes.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/status"

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

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_local_node_config(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Retrieve the local node configuration. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
            dict: The response containing information about the config of the local node.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/local/config"

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

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_local_node_apiconfig(self, pretty: bool = False, wait_for_complete: bool = False, nodes_list: list = None) -> dict: 
        """
        Returns the API configuration of all nodes (or a list) in JSON format. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
            nodes_list (list, optional): List of node IDs to filter results for (separated by commas). Defaults to None.

        Returns:
            dict: The response containing information about the sync status of specific nodes.
        """
         # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/api/config"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "nodes_list": ",".join(nodes_list) if nodes_list else None
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_node_status(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the status of all Wazuh daemons in node (node_id)

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The response containing information about the specified node.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/status"

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
    
    def get_node_info(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the status of all Wazuh daemons in node (node_id)

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The response containing information about the specified node.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/info"

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
    
    def get_node_config(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False, raw: bool = False,
                    section: str = None, field: str = None) -> dict:
        """
        Retrieve the Wazuh configuration used in the specified node.

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        raw (bool, optional): Format the response in plain text. Defaults to False.
        section (str, optional): Indicates the Wazuh configuration section. Valid values include:
            "active-response", "agentless", "alerts", "auth", "client", "client_buffer",
            "cluster", "command", "database_output", "email_alerts", "global", "integration",
            "labels", "localfile", "logging", "remote", "reports", "rootcheck", "ruleset",
            "sca", "socket", "syscheck", "syslog_output", "aws-s3", "azure-logs",
            "cis-cat", "docker-listener", "open-scap", "osquery", "syscollector",
            "vulnerability-detector". Defaults to None.
        field (str, optional): Indicates a section child (e.g., fields for ruleset section are
            decoder_dir, rule_dir, etc.). Defaults to None.

        Returns:
        dict: The response containing the configuration of the specified node.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/configuration"

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
        "section": section,
        "field": field
            }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def update_node_config(self, node_id: str, config_data: bytes, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Replace Wazuh configuration for the given node with the data contained in the API request.

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        config_data (bytes): The binary content of the ossec.conf to be uploaded. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The response containing information about the specified node.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/configuration"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/octet-stream"
         }

        # Prepare query parameters
        params = {
          "pretty": str(pretty).lower(),
          "wait_for_complete": str(wait_for_complete).lower()
          }

        # Send a PUT request to the endpoint with the request body (config_data)
        response = requests.put(endpoint, headers=headers, params=params, data=config_data)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_daemon_stats(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False, daemons_list: list = None):
        """
        Retrieve Wazuh statistical information from specified daemons in a specified cluster node.

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        daemons_list (list, optional): List of daemon names (e.g., "wazuh-analysisd", "wazuh-remoted", "wazuh-db").
            If not specified, all daemons will be selected by default.

        Returns:
        dict: The response containing the statistical information from the specified daemons in the specified node.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/daemons/stats"

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

        # Add daemons_list to params if provided
        if daemons_list:
            params["daemons_list"] = ",".join(daemons_list)

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_node_stats(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False, date: str = None) -> dict:
        """
        Return Wazuh statistical information in node (node_id) for the current or specified date

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        date (str, optional): Obtain stat info with the format YYYY-MM-DD

        Returns:
        dict: The response containing the statistical information from the specified daemons in the specified node.
        """
        
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/stats"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "date": str(date).lower()
            }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
        
        #Return the JSON response
        return response.json()
    
    def get_node_stat_hourly(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return Wazuh statistical information in hour node (node_id) for the current or specified date

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        date (str, optional): Obtain stat info with the format YYYY-MM-DD

        Returns:
        dict: The response containing the statistical information from the specified daemons in the specified node.
        """
        
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/stats/hourly"

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

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
        
        #Return the JSON response
        return response.json()

    def get_node_stat_weekly(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return Wazuh statistical information (weekly) for node (node_id) for the current or specified date

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        date (str, optional): Obtain stat info with the format YYYY-MM-DD

        Returns:
        dict: The response containing the statistical information from the specified daemons in the specified node.
        """
        
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/stats/weekly"

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

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
        
        #Return the JSON response
        return response.json()
    def get_node_logs(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, 
                  limit: int = 500, sort: str = None, search: str = None, tag: str = None, 
                  level: str = None, q: str = None, select: list = None, distinct: bool = False) -> dict:
        """
        Retrieve the last 2000 Wazuh log entries in the specified node.

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of lines to return (up to 500). Defaults to 500.
        sort (str, optional): Sort the collection by a field or fields (separated by comma).
            Use +/- at the beginning to list in ascending or descending order.
        search (str, optional): Look for elements containing the specified string.
            To obtain a complementary search, use '-' at the beginning.
        tag (str, optional): Wazuh component that logged the event.
        level (str, optional): Filter by log level. Valid values are "critical", "debug", "debug2", "error", "info", "warning".
        q (str, optional): Query to filter results by (e.g., "status=active").
        select (list, optional): List of fields to return (separated by commas).
            Use dot notation for nested fields (e.g., "field1.field2").
        distinct (bool, optional): Whether to look for distinct values. Defaults to False.

        Returns:
        dict: The response containing the last 2000 Wazuh log entries from the specified node.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/logs"

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
        "tag": tag,
        "level": level,
        "q": q,
        "select": ",".join(select) if select else None,
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
    
    def get_node_logs_summary(self, node_id: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return a summary of the last 2000 wazuh log entries in the specified node

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The response containing the statistical information from the specified daemons in the specified node.
        """
        
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/logs/summary"

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

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)
        
        #Return the JSON response
        return response.json()
    
    def restart_nodes(self, pretty: bool = False, wait_for_complete: bool = False, nodes_list: list = None) -> dict:
        """
        Restart all nodes in the cluster OR a list of them. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
            nodes_list (list, optional): List of node IDs to filter results for (separated by commas). Defaults to None.

        Returns:
            dict: The response containing information about the health of the specified nodes.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/restart"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "nodes_list": ",".join(nodes_list) if nodes_list else None
        }

        # Send a GET request to the endpoint
        response = requests.put(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def check_nodes_config(self, pretty: bool = False, wait_for_complete: bool = False, nodes_list: list = None) -> dict:
        """
        Return whether the Wazuh config is correct or not in all cluster nodes or a list of them. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
            nodes_list (list, optional): List of node IDs to filter results for (separated by commas). Defaults to None.

        Returns:
            dict: The response containing information about the health of the specified nodes.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/configuration/validation"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "nodes_list": ",".join(nodes_list) if nodes_list else None
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_node_active_configuration(self, node_id: str, component: str, configuration: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return the requested configuration in JSON format for the specified node.

        Parameters:
        node_id (str): Cluster node name. Required parameter.
        component (str): Selected agent's component. Required parameter.
            Valid values are "agent", "agentless", "analysis", "auth", "com", "csyslog", "integrator",
            "logcollector", "mail", "monitor", "request", "syscheck", "wazuh-db", "wmodules".
        configuration (str): Selected agent's configuration to read. Required parameter.
            Valid values depend on the component (refer to the documentation for the table of values).
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: The response containing the requested configuration in JSON format for the specified node.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/cluster/{node_id}/{component}/{configuration}"

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
