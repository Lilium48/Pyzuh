import requests
from errors import handle_errors

class Manager: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def get_status(self, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Returns the contents of all CDB lists. Optionally, the result can be filtered by several criteria. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        
        Returns:
        dict: A dictionary containing information about the Wazuh Manager. 
        """ 
        endpoint = f"{self.api_url}/manager/status"
        
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
    
    def get_information(self, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Returns basic information such as version, date, and install path. 

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        
        Returns:
        dict: A dictionary containing information about the Wazuh Manager. 
        """ 
        endpoint = f"{self.api_url}/manager/info"
        
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
    
    def get_configuration(self, pretty: bool = False, wait_for_complete: bool = False, section: str = False, raw: bool = False) -> dict:
        """
        Fetch the configuration from the API.

        Parameters:
        pretty (bool, optional): Return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Wait for the request to complete without timing out. Defaults to False.
        section (str): The configuration section to fetch. Enum: See documentation for possible values.
        raw (bool, optional): Return response in plain text format. Defaults to False.

        Returns:
        dict: A dictionary containing the content of the specified configuration section.
        
        Raises:
        HTTPError: If there is an error in the response.
        """
        # Construct endpoint URL
        endpoint = f"{self.api_url}/manager/configuration"

        # Define request headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Define request parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "raw": str(raw).lower(),
            "section": section
        }

        # Perform the GET request
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()  # Parse and return the JSON response

        except requests.RequestException as e:
            # Handle request errors (e.g., network issues, authentication errors)
            handle_errors(response)  # Use handle_errors function to manage the error
            raise  # Reraise the exception to alert the caller
        
    def update_config(self, pretty: bool = False, wait_for_complete: bool = False) -> dict: 
        """
        Fetch the configuration from the API.

        Parameters:
        pretty (bool, optional): Return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Wait for the request to complete without timing out. Defaults to False.
        
        Returns:
        dict: A dictionary containing the content of the specified configuration section.
        """
       
        #Declare endpoint for interaction
        endpoint = f"{self.api_url}/manager/configuration"
        
        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/octet-stream"
         }

        #Define Params 
        params = { 
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower()
        }
        
        #Put request to the Wazuh API
        response = requests.put(endpoint, headers=headers, params=params)
        
        #Error Handling, calls function
        handle_errors(response)
        
        # Return the response
        return response.json

    def get_daemon_stats(self, pretty: bool = False, wait_for_complete: bool = False, daemons_list: list[str] = None) -> dict:
        """
        Get Wazuh statistical information from specified daemons.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        daemons_list (List[str], optional): List of daemon names. Enum: "wazuh-analysisd", "wazuh-remoted", "wazuh-db".
            All daemons selected by default if not specified.

        Returns:
        dict: A dictionary containing the statistical information from the specified daemons.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/daemons/stats"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "daemons_list": ','.join(daemons_list) if daemons_list else None
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_stats(self, pretty: bool = False, wait_for_complete: bool = False, date: str = None) -> dict:
        """
        Get Wazuh statistical information for the current or specified date.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        date (str, optional): Date to obtain statistical information from. Format YYYY-MM-DD.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/stats"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "date": date
        }

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_stats_hour(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Get Wazuh statistical information for the current or specified date.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        date (str, optional): Date to obtain statistical information from. Format YYYY-MM-DD.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/stats/hourly"

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
    
    def get_stats_weekly(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Get Wazuh statistical information for the current or specified date.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        date (str, optional): Date to obtain statistical information from. Format YYYY-MM-DD.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/stats/weekly"

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
    
    def get_logs(self, pretty: bool, wait_for_complete: bool, offset: int, limit: int, sort: str = None, search: str = None, tag: str = None, level: str = None, q: str = None, select: str = None, distinct: bool = False) -> dict:
        """
        Get the last 2000 Wazuh log entries.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): The starting index of log entries to return. Defaults to 0.
        limit (int, optional): The maximum number of log entries to return. Defaults to 2000.
        sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Defaults to None.
        tag (str, optional): Wazuh component that logged the event. Defaults to None.
        level (str, optional): Filter by log level. Enum: "critical", "debug", "debug2", "error", "info", "warning". Defaults to None.
        q (str, optional): Query to filter results by. Defaults to None.
        select (str, optional): Select which fields to return. Defaults to None.
        distinct (bool, optional): Look for distinct values. Defaults to False.

        Returns:
        dict: A dictionary containing the last 2000 Wazuh log entries.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/logs"

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
            "select": select,
            "distinct": str(distinct).lower()
        }
        
        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors in the response
        handle_errors(response)
        
        # Parse and return the JSON response
        return response.json()
    
    def get_logs_summary(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Get logs summary. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/logs/summary"

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
        
    def get_api_config(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return local api config. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/stats/weekly"

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

    def restart_manager(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Get Wazuh statistical information for the current or specified date.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/restart"

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
        
    def check_config(self, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Return local api config. 

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the statistical information for the specified date.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/manager/configuration/validation"

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
        
    def get_active_config(self, component: str, configuration: str, pretty: bool = False, wait_for_complete: bool = False) -> dict:
        """
        Get the requested active configuration in JSON format.

        Parameters:
        component (str): Selected agent's component. Enum: "agent", "agentless", "analysis", "auth", "com", "csyslog", "integrator", "logcollector", "mail", "monitor", "request", "syscheck", "wazuh-db", "wmodules".
        configuration (str): Selected agent's configuration to read. Enum depends on the selected component.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.

        Returns:
        dict: A dictionary containing the requested active configuration in JSON format.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/wazuh/configuration/{component}/{configuration}"

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