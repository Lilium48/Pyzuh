import requests
from errors import handle_errors

class Experimental:
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def clear_rootcheck_results(self, pretty: bool = False, agents_list: str = None, wait_for_complete: bool = False) -> dict:
        """
        Clear rootcheck database for all agents or a specific list of agents.

        Parameters:
            agents_list (str, optional): List of agent IDs, or use the keyword "all" to select all agents.
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
            dict: The response from the server.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/rootcheck"

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

        # Send a DELETE request to the endpoint
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def clear_agent_FIM(self, pretty: bool = False, agents_list: str = None, wait_for_complete: bool = False) -> dict:
        """
        Clear the syscheck database for all agents or a list. 

        Parameters:
            agents_list (str, optional): List of agent IDs, or use the keyword "all" to select all agents.
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.

        Returns:
            dict: The response from the server.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/syscheck"

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

        # Send a DELETE request to the endpoint
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def get_agents_ciscat_results(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list = None, offset: int = 0, limit: int = 500,
                             sort: str = None, search: str = None, select: list = None, benchmark: str = None, profile: str = None,
                             pass_checks: int = 0, fail_checks: int = 0, error_checks: int = 0, notchecked_checks: int = 0,
                             unknown_results: int = 0, score: int = 0) -> dict:
        """
        Retrieve CIS-CAT results for all agents or a list of specified agents.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        agents_list (list, optional): List of agent IDs (comma-separated strings). All agents are selected by default if not specified. Defaults to None.
        offset (int, optional): The first element to return in the collection. Must be >= 0. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500. Up to 100,000 can be specified, but exceeding 500 elements may slow responses.
        sort (str, optional): Criteria for sorting the collection (e.g., '+field' or '-field'). Defaults to None.
        search (str, optional): Look for elements containing the specified string. Use '-' for complementary search. Defaults to None.
        select (list, optional): Fields to return (comma-separated strings). Use '.' for nested fields (e.g., 'field1.field2'). Defaults to None.
        benchmark (str, optional): Filter results by benchmark type. Defaults to None.
        profile (str, optional): Filter results by evaluated profile. Defaults to None.
        pass_checks (int, optional): Filter by the number of passed checks. Must be >= 0. Defaults to 0.
        fail_checks (int, optional): Filter by the number of failed checks. Must be >= 0. Defaults to 0.
        error_checks (int, optional): Filter by the number of encountered errors. Must be >= 0. Defaults to 0.
        notchecked_checks (int, optional): Filter by the number of unchecked results. Must be >= 0. Defaults to 0.
        unknown_results (int, optional): Filter by unknown results. Defaults to 0.
        score (int, optional): Filter by final score. Must be >= 0. Defaults to 0.

        Returns:
        dict: A dictionary containing the CIS-CAT results for the specified agents.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/ciscat/results"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
            }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": ",".join(agents_list) if agents_list else None,
        "offset": offset,
        "limit": limit,
        "sort": sort,
        "search": search,
        "select": ",".join(select) if select else None,
        "benchmark": benchmark,
        "profile": profile,
        "pass": pass_checks,
        "fail": fail_checks,
        "error": error_checks,
        "notchecked": notchecked_checks,
        "unknown": unknown_results,
        "score": score
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_agent_hardware(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list = None, offset: int = 0, limit: int = 500,
                       sort: str = None, search: str = None, select: list = None, ram_free: int = 0, ram_total: int = 0, cpu_cores: int = 1,
                       cpu_mhz: float = 1, cpu_name: str = None, board_serial: str = None) -> dict:
        """
        Retrieve hardware information for all agents or a list of specified agents.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        agents_list (list, optional): List of agent IDs (comma-separated strings). All agents are selected by default if not specified. Defaults to None.
        offset (int, optional): The first element to return in the collection. Must be >= 0. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500. Although up to 100,000 can be specified, it is recommended not to exceed 500.
        sort (str, optional): Criteria for sorting the collection (e.g., '+field' or '-field'). Defaults to None.
        search (str, optional): Look for elements containing the specified string. Use '-' for complementary search. Defaults to None.
        select (list, optional): Fields to return (comma-separated strings). Use '.' for nested fields (e.g., 'field1.field2'). Defaults to None.
        ram_free (int, optional): Filter by available RAM. Must be >= 0. Defaults to 0.
        ram_total (int, optional): Filter by total RAM. Must be >= 0. Defaults to 0.
        cpu_cores (int, optional): Filter by number of CPU cores. Must be >= 1. Defaults to 1.
        cpu_mhz (float, optional): Filter by CPU frequency in MHz. Must be >= 1. Defaults to 1.
        cpu_name (str, optional): Filter by CPU name. Defaults to None.
        board_serial (str, optional): Filter by board serial number. Defaults to None.

        Returns:
        dict: A dictionary containing the hardware information of the specified agents.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/syscollector/hardware"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
            }

        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": ",".join(agents_list) if agents_list else None,
        "offset": str(offset),
        "limit": str(limit),
        "sort": sort,
        "search": search,
        "select": ",".join(select) if select else None,
        "ram_free": str(ram_free) if ram_free != 0 else None,
        "ram_total": str(ram_total) if ram_total != 0 else None,
        "cpu_cores": str(cpu_cores) if cpu_cores != 1 else None,
        "cpu_mhz": str(cpu_mhz) if cpu_mhz != 1 else None,
        "cpu_name": cpu_name,
        "board_serial": board_serial
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}


        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def get_agents_netiface(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list = None, offset: int = 0,
                            limit: int = 500, sort: str = None, search: str = None, select: list = None, name: str = None,
                            adapter: str = None, type: str = None, state: str = None, mtu: int = None, tx_packets: int = None,
                            rx_packets: int = None, tx_bytes: int = None, rx_bytes: int = None, tx_errors: int = None,
                            rx_errors: int = None, tx_dropped: int = None, rx_dropped: int = None) -> dict:
        """
        Return all agents (or a list of them) network interfaces. This information includes rx, scan, tx information, and other network information.

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
            agents_list (list, optional): List of agent IDs (comma-separated). Defaults to None.
            offset (int, optional): First element to return in the collection. Defaults to 0.
            limit (int, optional): Maximum number of elements to return. Defaults to 500.
            sort (str, optional): Criteria for sorting the results. Defaults to None.
            search (str, optional): Look for elements containing the specified string. Defaults to None.
            select (list, optional): List of fields to return (comma-separated). Defaults to None.
            name (str, optional): Filter by network interface name. Defaults to None.
            adapter (str, optional): Filter by adapter. Defaults to None.
            type (str, optional): Filter by network type. Defaults to None.
            state (str, optional): Filter by network state. Defaults to None.
            mtu (int, optional): Filter by MTU. Defaults to None.
            tx_packets (int, optional): Filter by transmitted packets. Defaults to None.
            rx_packets (int, optional): Filter by received packets. Defaults to None.
            tx_bytes (int, optional): Filter by transmitted bytes. Defaults to None.
            rx_bytes (int, optional): Filter by received bytes. Defaults to None.
            tx_errors (int, optional): Filter by transmitted errors. Defaults to None.
            rx_errors (int, optional): Filter by received errors. Defaults to None.
            tx_dropped (int, optional): Filter by transmitted dropped packets. Defaults to None.
            rx_dropped (int, optional): Filter by received dropped packets. Defaults to None.

        Returns:
            dict: The response containing the agents' network interface information.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/netiface"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "agents_list": ",".join(agents_list) if agents_list else None,
            "offset": str(offset),
            "limit": str(limit),
            "sort": sort,
            "search": search,
            "select": ",".join(select) if select else None,
            "name": name,
            "adapter": adapter,
            "type": type,
            "state": state,
            "mtu": str(mtu) if mtu is not None else None,
            "tx.packets": str(tx_packets) if tx_packets is not None else None,
            "rx.packets": str(rx_packets) if rx_packets is not None else None,
            "tx.bytes": str(tx_bytes) if tx_bytes is not None else None,
            "rx.bytes": str(rx_bytes) if rx_bytes is not None else None,
            "tx.errors": str(tx_errors) if tx_errors is not None else None,
            "rx.errors": str(rx_errors) if rx_errors is not None else None,
            "tx.dropped": str(tx_dropped) if tx_dropped is not None else None,
            "rx.dropped": str(rx_dropped) if rx_dropped is not None else None,
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_agents_netaddr(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list = None, offset: int = 0, limit: int = 500,
                       sort: str = None, select: str = None, search: str = None, proto: str = None, address: str = None, broadcast: str = None, netmask: str = None) -> dict:
        """
        Retrieve hardware information for all agents or a list of specified agents.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        agents_list (list, optional): List of agent IDs (comma-separated strings). All agents are selected by default if not specified. Defaults to None.
        offset (int, optional): The first element to return in the collection. Must be >= 0. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Defaults to 500. Although up to 100,000 can be specified, it is recommended not to exceed 500.
        sort (str, optional): Criteria for sorting the collection (e.g., '+field' or '-field'). Defaults to None.
        search (str, optional): Look for elements containing the specified string. Use '-' for complementary search. Defaults to None.
        select (list, optional): Fields to return (comma-separated strings). Use '.' for nested fields (e.g., 'field1.field2'). Defaults to None.
        proto (str, optional): Field to filter to by IP Protocol. 
        address (str, optional): Filter by IP address. 
        broadcast (str, optional): Filter by broadcast direction. Defaults to None. 
        netmask (str, optional): Filter by netmask. 
        
        Returns:
        dict: A dictionary containing the hardware information of the specified agents.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/syscollector/netaddr"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
            }

        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": ",".join(agents_list) if agents_list else None,
        "offset": str(offset),
        "limit": str(limit),
        "sort": sort,
        "search": search,
        "select": ",".join(select) if select else None,
        "proto": proto,
        "address": address,
        "broadcast": broadcast,
        "netmask": netmask
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}
        
        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_agents_netproto(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list[str] = None, offset: int = 0,
                            limit: int = 500, sort: str = None, search: str = None, select: list = None, iface: str = None,
                            type: str = None, gateway: str = None, dhcp: str = None) -> dict:
        """
        Return all agents (or a list of them) routing configuration for each network interface. This information includes
        interface, type protocol information, and other data.

        Parameters:
            pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
            agents_list (list, optional): List of agent IDs (comma-separated), all agents selected by default if not specified. Defaults to None.
            offset (int, optional): First element to return in the collection. Defaults to 0.
            limit (int, optional): Maximum number of elements to return. Defaults to 500.
            sort (str, optional): Sort the collection by a field or fields (comma-separated). Use +/- at the beginning for ascending or descending order. Defaults to None.
            search (str, optional): Look for elements containing the specified string. Use '-' at the beginning for complementary search. Defaults to None.
            select (list, optional): Fields to return (comma-separated). Use '.' for nested fields. Defaults to None.
            iface (str, optional): Filter by network interface. Defaults to None.
            type (str, optional): Filter by type of network. Defaults to None.
            gateway (str, optional): Filter by network gateway. Defaults to None.
            dhcp (str, optional): Filter by network DHCP status (enabled, disabled, unknown, BOOTP). Defaults to None.

        Returns:
            dict: The response containing the agents' netproto information.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/syscollector/netproto"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "agents_list": ",".join(agents_list) if agents_list else None,
            "offset": str(offset),
            "limit": str(limit),
            "sort": sort,
            "search": search,
            "select": ",".join(select) if select else None,
            "iface": iface,
            "type": type,
            "gateway": gateway,
            "dhcp": dhcp
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_agents_os(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list[str] = None,
                  offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
                  select: list[str] = None, os_name: str = None, architecture: str = None,
                  os_version: str = None, version: str = None, release: str = None) -> dict:
        """
        Get OS information of agents from the Wazuh API.

        Parameters:
        - pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        - agents_list (list[str], optional): A list of agent IDs to target. Defaults to None (all agents).
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500.
        - sort (str, optional): Sort the collection by a field or fields. Defaults to None.
        - search (str, optional): Search for elements containing the specified string. Defaults to None.
        - select (list[str], optional): Fields to return in the response. Defaults to None.
        - os_name (str, optional): Filter by OS name. Defaults to None.
        - architecture (str, optional): Filter by architecture. Defaults to None.
        - os_version (str, optional): Filter by OS version. Defaults to None.
        - version (str, optional): Filter by agents' version using various formats (e.g. 'X.Y.Z'). Defaults to None.
        - release (str, optional): Filter by release. Defaults to None.

        Returns:
        - dict: A dictionary containing the OS information of agents.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/syscollector/os"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": ",".join(agents_list) if agents_list else None,
        "offset": str(offset),
        "limit": str(limit),
        "sort": sort,
        "search": search,
        "select": ",".join(select) if select else None,
        "os.name": os_name,
        "architecture": architecture,
        "os.version": os_version,
        "version": version,
        "release": release
        }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        self.handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_agents_packages(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list[str] = None,
                        offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
                        select: list[str] = None, vendor: str = None, name: str = None,
                        architecture: str = None, format: str = None, version: str = None) -> dict:
        """
        Return all agents (or a list of them) packages info. This information includes name, section, size,
        and priority information of all packages among other data.

        Parameters:
        - pretty (bool, optional): Whether to show results in human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - agents_list (List[str], optional): List of agent IDs (comma-separated). Defaults to None (all agents).
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500.
        - sort (str, optional): Sort the collection by a field or fields (comma-separated). Defaults to None.
        - search (str, optional): Search for elements containing the specified string. Defaults to None.
        - select (List[str], optional): Fields to return (comma-separated). Defaults to None.
        - vendor (str, optional): Filter by vendor. Defaults to None.
        - name (str, optional): Filter by name. Defaults to None.
        - architecture (str, optional): Filter by architecture. Defaults to None.
        - format (str, optional): Filter by file format (e.g. 'deb'). Defaults to None.
        - version (str, optional): Filter by package version. Defaults to None.

        Returns:
        - Dict[str, Union[dict, list]]: A dictionary containing the packages information of agents.
         """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/syscollector/packages"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
         }

        # Prepare the query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": ','.join(agents_list) if agents_list else None,
        "offset": str(offset),
        "limit": str(limit),
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "vendor": vendor,
        "name": name,
        "architecture": architecture,
        "format": format,
        "version": version
        }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def get_agents_ports(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list[str] = None,
                     offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
                     select: list[str] = None, pid: str = None, protocol: str = None,
                     local_ip: str = None, local_port: str = None, remote_ip: str = None,
                     tx_queue: str = None, state: str = None, process: str = None) -> dict:
        """
        Return all agents (or a list of them) ports information. This includes details such as local IP, remote IP,
        protocol information, and other data.

        Parameters:
        - pretty (bool, optional): Whether to show results in human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - agents_list (list[str], optional): List of agent IDs to target (comma-separated). Defaults to None (all agents).
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500.
        - sort (str, optional): Sort the collection by a field or fields (comma-separated). Defaults to None.
        - search (str, optional): Search for elements containing the specified string. Defaults to None.
        - select (list[str], optional): Fields to return (comma-separated). Defaults to None.
        - pid (str, optional): Filter by PID. Defaults to None.
        - protocol (str, optional): Filter by protocol. Defaults to None.
        - local_ip (str, optional): Filter by Local IP. Defaults to None.
        - local_port (str, optional): Filter by Local Port. Defaults to None.
        - remote_ip (str, optional): Filter by Remote IP. Defaults to None.
        - tx_queue (str, optional): Filter by tx_queue. Defaults to None.
        - state (str, optional): Filter by state. Defaults to None.
        - process (str, optional): Filter by process name. Defaults to None.

        Returns:
        - dict: A dictionary containing the ports information of agents.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/agents/ports"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": ','.join(agents_list) if agents_list else None,
        "offset": offset,
        "limit": limit,
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "pid": pid,
        "protocol": protocol,
        "local.ip": local_ip,
        "local.port": local_port,
        "remote.ip": remote_ip,
        "tx_queue": tx_queue,
        "state": state,
        "process": process
    }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def get_agents_processes(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list[str] = None,
                        offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
                        select: list[str] = None, pid: str = None, state: str = None, ppid: str = None,
                        egroup: str = None, euser: str = None, fgroup: str = None, name: str = None,
                        nlwp: str = None, pgrp: str = None, priority: str = None, rgroup: str = None,
                        ruser: str = None, sgroup: str = None, suser: str = None) -> dict:
        """
        Return all agents (or a list of them) processes information.

        Parameters:
        - pretty (bool, optional): Whether to show results in human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - agents_list (list[str], optional): List of agent IDs to target (comma-separated). Defaults to None (all agents).
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500.
        - sort (str, optional): Sort the collection by a field or fields (comma-separated). Defaults to None.
        - search (str, optional): Search for elements containing the specified string. Defaults to None.
        - select (list[str], optional): Fields to return (comma-separated). Defaults to None.
        - pid (str, optional): Filter by process PID. Defaults to None.
        - state (str, optional): Filter by process state. Defaults to None.
        - ppid (str, optional): Filter by process parent PID. Defaults to None.
        - egroup (str, optional): Filter by process egroup. Defaults to None.
        - euser (str, optional): Filter by process euser. Defaults to None.
        - fgroup (str, optional): Filter by process fgroup. Defaults to None.
        - name (str, optional): Filter by process name. Defaults to None.
        - nlwp (str, optional): Filter by process nlwp. Defaults to None.
        - pgrp (str, optional): Filter by process pgrp. Defaults to None.
        - priority (str, optional): Filter by process priority. Defaults to None.
        - rgroup (str, optional): Filter by process rgroup. Defaults to None.
        - ruser (str, optional): Filter by process ruser. Defaults to None.
        - sgroup (str, optional): Filter by process sgroup. Defaults to None.
        - suser (str, optional): Filter by process suser. Defaults to None.

        Returns:
        - dict: A dictionary containing the processes information of agents.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/syscollector/processes"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": ','.join(agents_list) if agents_list else None,
        "offset": str(offset),
        "limit": str(limit),
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "pid": pid,
        "state": state,
        "ppid": ppid,
        "egroup": egroup,
        "euser": euser,
        "fgroup": fgroup,
        "name": name,
        "nlwp": nlwp,
        "pgrp": pgrp,
        "priority": priority,
        "rgroup": rgroup,
        "ruser": ruser,
        "sgroup": sgroup,
        "suser": suser
        }   

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()

    def get_agents_hotfixes(self, pretty: bool = False, wait_for_complete: bool = False, agents_list: list[str] = None,
                        offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
                        select: list[str] = None, hotfix: str = None) -> dict:
        """
        Return all agents (or a list of them) hotfixes information.

        Parameters:
        - pretty (bool, optional): Whether to show results in human-readable format. Defaults to False.
        - wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        - agents_list (list[str], optional): List of agent IDs to target (comma-separated). Defaults to None (all agents).
        - offset (int, optional): First element to return in the collection. Defaults to 0.
        - limit (int, optional): Maximum number of elements to return. Defaults to 500.
        - sort (str, optional): Sort the collection by a field or fields (comma-separated). Defaults to None.
        - search (str, optional): Search for elements containing the specified string. Defaults to None.
        - select (list[str], optional): Fields to return (comma-separated). Defaults to None.
        - hotfix (str, optional): Filter by hotfix. Defaults to None.

        Returns:
        - dict: A dictionary containing the hotfixes information of agents.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/experimental/syscollector/hotfixes"

        # Create headers for the API request
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare the query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "agents_list": ','.join(agents_list) if agents_list else None,
        "offset": offset,
        "limit": limit,
        "sort": sort,
        "search": search,
        "select": ','.join(select) if select else None,
        "hotfix": hotfix
        }

        # Filter out None values from the params dictionary
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Parse and return the JSON response
        return response.json()
