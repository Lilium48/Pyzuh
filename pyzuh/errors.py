def handle_errors(self, response):
    """Handle errors from the API response and raise exceptions accordingly."""
    status_code = response.status_code
    
    if status_code == 400:
        error_info = response.json()
        title = error_info.get("title", "Bad Request")
        detail = error_info.get("detail", "")
        error_code = error_info.get("error", 0)
        raise ValueError(f"Bad Request: {title}. Detail: {detail}. Error Code: {error_code}.")
    
    elif status_code == 401:
        error_info = response.json()
        title = error_info.get("title", "Unauthorized Request")
        detail = error_info.get("detail", "")
        error_code = error_info.get("error", 0)
        error_message = f"Unauthorized request: {title}. Detail: {detail}. Error Code: {error_code}."
        raise PermissionError(error_message)
    
    elif status_code == 403:
        # Parse the 403 response details
        error_info = response.json()
        title = error_info.get("title", "Permission Denied")
        detail = error_info.get("detail", "")
        instance = error_info.get("instance", "")
        code = error_info.get("code", 0)
        remediation = error_info.get("remediation", "")
        dapi_errors = error_info.get("dapi_errors", {})
        
        # Construct an informative error message
        error_message = (f"Permission denied: {title}. Detail: {detail}. Instance: {instance}. "
                         f"Code: {code}. Remediation: {remediation}. DAPI Errors: {dapi_errors}.")
        
        # Raise PermissionError with the detailed error message
        raise PermissionError(error_message)
    
    elif status_code == 405:
        error_info = response.json()
        title = error_info.get("title", "Invalid HTTP Method")
        detail = error_info.get("detail", "")
        error_code = error_info.get("error", 0)
        raise PermissionError(f"Invalid HTTP Method: {title}. Detail: {detail}. Error Code: {error_code}.")
    
    elif status_code == 429:
        error_info = response.json()
        title = error_info.get("title", "Maximum Requests Per Minute Reached")
        detail = error_info.get("detail", "")
        error_code = error_info.get("error", 0)
        raise PermissionError(f"Maximum requests per minute reached: {title}. Detail: {detail}. Error Code: {error_code}.")
    
    else:
        response.raise_for_status()  # Raise an HTTPError for other status codes
