import requests
from errors import handle_errors
import jwt 

class Decoders: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def list_decoders(self, decoder_names: list = None, pretty: bool = False, wait_for_complete: bool = False, 
                  offset: int = 0, limit: int = 500, select: list = None, sort: str = None, 
                  search: str = None, q: str = None, filename: list = None, relative_dirname: str = None, 
                  status: str = None, distinct: bool = False) -> dict:
        """
        Return information about all decoders included in ossec.conf. This information includes decoder's route, name, file, among others.

        Parameters:
        decoder_names (list, optional): List of decoder names. Defaults to None.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return (up to 500). Defaults to 500.
        select (list, optional): List of fields to return (comma-separated string). Defaults to None.
        sort (str, optional): Field(s) to sort by (comma-separated). Use +/- for ascending/descending. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Use '-' for complementary search. Defaults to None.
        q (str, optional): Query to filter results by (e.g., "status=active"). Defaults to None.
        filename (list, optional): List of filenames to filter by. Defaults to None.
        relative_dirname (str, optional): Filter by relative directory name. Defaults to None.
        status (str, optional): Filter by list status ("enabled", "disabled", "all"). Defaults to None.
        distinct (bool, optional): Whether to look for distinct values. Defaults to False.

        Returns:
        dict: The response containing information about all decoders included in ossec.conf.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/decoders"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "decoder_names": ",".join(decoder_names) if decoder_names else None,
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "offset": offset,
            "limit": limit,
            "select": ",".join(select) if select else None,
            "sort": sort,
            "search": search,
            "q": q,
            "filename": ",".join(filename) if filename else None,
            "relative_dirname": relative_dirname,
            "status": status,
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
    
    def get_files(self, decoder_names: list = None, pretty: bool = False, wait_for_complete: bool = False, 
                  offset: int = 0, limit: int = 500, select: list = None, sort: str = None, 
                  search: str = None, q: str = None, filename: list = None, relative_dirname: str = None, 
                  status: str = None, distinct: bool = False) -> dict:
        """
        Return information about all decoders included in ossec.conf. This information includes decoder's route, name, file, among others.

        Parameters:
        decoder_names (list, optional): List of decoder names. Defaults to None.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to disable timeout response. Defaults to False.
        offset (int, optional): First element to return in the collection. Defaults to 0.
        limit (int, optional): Maximum number of elements to return (up to 500). Defaults to 500.
        select (list, optional): List of fields to return (comma-separated string). Defaults to None.
        sort (str, optional): Field(s) to sort by (comma-separated). Use +/- for ascending/descending. Defaults to None.
        search (str, optional): Look for elements containing the specified string. Use '-' for complementary search. Defaults to None.
        q (str, optional): Query to filter results by (e.g., "status=active"). Defaults to None.
        filename (list, optional): List of filenames to filter by. Defaults to None.
        relative_dirname (str, optional): Filter by relative directory name. Defaults to None.
        status (str, optional): Filter by list status ("enabled", "disabled", "all"). Defaults to None.
        distinct (bool, optional): Whether to look for distinct values. Defaults to False.

        Returns:
        dict: The response containing information about all decoders included in ossec.conf.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/decoders/files"

        # Create headers
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
            "decoder_names": ",".join(decoder_names) if decoder_names else None,
            "pretty": str(pretty).lower(),
            "wait_for_complete": str(wait_for_complete).lower(),
            "offset": offset,
            "limit": limit,
            "select": ",".join(select) if select else None,
            "sort": sort,
            "search": search,
            "q": q,
            "filename": ",".join(filename) if filename else None,
            "relative_dirname": relative_dirname,
            "status": status,
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

    def get_file_content(self, filename: str, pretty: bool = False, wait_for_complete: bool = False, raw: bool = False, relative_dirname: str = None) -> dict:
        """
        Retrieve the content of a specified decoder file.

        Parameters:
        filename (str): Filename (rule or decoder) to download/upload/edit file. Required.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        raw (bool, optional): Whether to return the content in raw format. Defaults to False.
        relative_dirname (str, optional): Relative directory name of the files to filter by. Defaults to None.

        Returns:
        dict: A dictionary containing the content of the specified file.
        """
        
        # Define the endpoint URL
        endpoint = f"{self.api_url}/decoders/files/{filename}"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/json"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "relative_dirname": relative_dirname,
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    
    def update_file_content(self, filename: str, pretty: bool = False, wait_for_complete: bool = False, overwrite: bool = False, relative_dirname: str = None, file_content: bytes = None) -> dict:
        """
        Upload or replace the content of a user decoder file.

        Parameters:
        filename (str): The filename (rule or decoder) to upload or edit.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        overwrite (bool, optional): If set to False, an exception will be raised when updating contents of an already existing filename. Defaults to False.
        relative_dirname (str, optional): Relative directory name to filter by. Defaults to None.

        Returns:
        dict: A dictionary containing the response from the server after updating the file content.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/decoders/files/{filename}"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}",
        "Content-Type": "application/octet-stream"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "overwrite": str(overwrite).lower(),
        "relative_dirname": relative_dirname
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a PUT request to the endpoint with the file content as data
        response = requests.put(endpoint, headers=headers, params=params, data=file_content)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()

    def delete_file_content(self, filename: str, pretty: bool = False, wait_for_complete: bool = False, relative_dirname: str = None) -> dict:
        """
        Delete a specified decoder file.

        Parameters:
        filename (str): The filename (rule or decoder) to delete.
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        relative_dirname (str, optional): Relative directory name of the file to filter by. Defaults to None.

        Returns:
        dict: A dictionary containing the response from the server.
        """
        # Define the endpoint URL
        endpoint = f"{self.api_url}/decoders/files/{filename}"

        # Create headers
        headers = {
        "Authorization": f"Bearer {self.jwt_token}"
        }

        # Prepare query parameters
        params = {
        "pretty": str(pretty).lower(),
        "wait_for_complete": str(wait_for_complete).lower(),
        "relative_dirname": relative_dirname
        }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a DELETE request to the endpoint
        response = requests.delete(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
    
    def get_parent_decoders(self, pretty: bool = False, wait_for_complete: bool = False, offset: int = 0, limit: int = 500, 
                        select: list = None, sort: str = None, search: str = None) -> dict:
        """
        Return information about all parent decoders. A parent decoder is a decoder used as the base of other decoders.

        Parameters:
        pretty (bool, optional): Whether to return the response in a human-readable format. Defaults to False.
        wait_for_complete (bool, optional): Whether to wait for the operation to complete. Defaults to False.
        offset (int, optional): First element to return in the collection. Must be greater than or equal to 0. Defaults to 0.
        limit (int, optional): Maximum number of elements to return. Recommended not to exceed 500 elements. Defaults to 500.
        select (list, optional): List of fields to return (comma-separated string). Use '.' for nested fields (e.g., 'field1.field2'). Defaults to None.
        sort (str, optional): Sort the collection by a field or fields (comma-separated string). Use +/- for ascending/descending order. Use '.' for nested fields. Defaults to None.
        search (str, optional): Search for elements containing the specified string. Use '-' at the beginning for complementary search. Defaults to None.

        Returns:
        dict: A dictionary containing information about all parent decoders.
        """

        
        # Define the endpoint URL
        endpoint = f"{self.api_url}/decoders/parents"

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
            "select": ",".join(select) if select else None,
            "sort": sort,
            "search": search,
            }

        # Filter out parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)

        # Handle errors in the response
        handle_errors(response)

        # Parse and return the JSON response
        return response.json()
