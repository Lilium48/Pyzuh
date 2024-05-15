import requests
import jwt
import json
from errors import handle_errors

class Ciscat: 
    def __init__(self, api_url: str, jwt_token: str):
        self.api_url = api_url
        self.jwt_token = jwt_token
    
    def get_results(self, agent_id: str, pretty: bool = False, wait_for_complete: bool = False, 
                    offset: int = 0, limit: int = 500, sort: str = None, search: str = None,
                    select: list = None, benchmark: str = None, profile: str = None,
                    pass_: int = None, fail: int = None, error: int = None,
                    notchecked: int = None, unknown: int = None, score: int = None, q: str = None):
        """
        Get results of the agent's CIS-CAT scans.

        Args:
            agent_id (str): The agent ID to get results for.
            pretty (bool, optional): Whether to return human-readable format. Defaults to False.
            wait_for_complete (bool, optional): Whether to wait for completion of the operation. Defaults to False.
            offset (int, optional): Offset for the collection. Defaults to 0.
            limit (int, optional): Limit for the collection size. Defaults to 500.
            sort (str, optional): Sort criteria for the results.
            search (str, optional): Search string for filtering results.
            select (list, optional): List of fields to return.
            benchmark (str, optional): Filter by benchmark type.
            profile (str, optional): Filter by profile type.
            pass_ (int, optional): Filter by number of passed checks.
            fail (int, optional): Filter by number of failed checks.
            error (int, optional): Filter by number of errors encountered.
            notchecked (int, optional): Filter by number of unchecked results.
            unknown (int, optional): Filter by unknown results.
            score (int, optional): Filter by final score.
            q (str, optional): Additional query filter.
        
        Returns:
            dict: The agent's CIS-CAT results.
        """
        # Build the endpoint URL
        endpoint = f"{self.api_url}/ciscat/{agent_id}/results"
        
        # Prepare headers with the JWT token for authorization
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json",
        }

        # Prepare query parameters
        params = {
            "pretty": pretty,
            "wait_for_complete": wait_for_complete,
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "search": search,
            "select": ",".join(select) if select else None,
            "benchmark": benchmark,
            "profile": profile,
            "pass": pass_,
            "fail": fail,
            "error": error,
            "notchecked": notchecked,
            "unknown": unknown,
            "score": score,
            "q": q,
        }

        # Remove parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Send a GET request to the endpoint
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Handle errors
        handle_errors(response)
        
        # Parse and return JSON response
        return response.json()