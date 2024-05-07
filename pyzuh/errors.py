# Python Code for Error Handling. Each function of the library calls upon this function if an error is raised when a request is made. 

def handle_errors(self, response):
    """Handle errors from the API response and raise exceptions accordingly."""
    status_code = response.status_code
    
    if status_code == 400:
        error_info = response.json()
        title = error_info.get("title", "Bad Request")
        detail = error_info.get("detail", "'{invalid_param}' is not a '{expected_type}'. Failed validating 'format' in schema['items']: {'description': '{parameter_name}', 'format': '{expected_format}', 'minLength': {expected_length}, 'type': '{expected_type}', 'x-scope': ['', '#/components/parameters/{parameter_name}']}")
        raise ValueError(f"Bad Request: {title}. Detail: {detail}.")
    
    elif status_code == 401:
        error_info = response.json()
        title = error_info.get("title", "Unauthorized Request")
        detail = error_info.get("detail", "No authorization token provided")
        error_message = f"Unauthorized request: {title}. Detail: {detail}."
        raise PermissionError(error_message)
    
    elif status_code == 403:
        error_info = response.json()
        title = error_info.get("title", "Permission Denied")
        detail = error_info.get("detail", "Permission denied: Resource type *:*")
        remediation = error_info.get("remediation", "Please make sure you have permissions to execute the current request.")
        code = error_info.get("error", 4000)
        dapi_errors = error_info.get("dapi_errors", {})

        # Construct an informative error message
        error_message = (f"Permission denied: {title}. Detail: {detail}. "
                     f"Code: {code}. Remediation: {remediation}. "
                     f"DAPI Errors: {dapi_errors}.")

        # Raise a PermissionError with the constructed error message
        raise PermissionError(error_message)
    
    elif status_code == 405:
        error_info = response.json()
        title = error_info.get("title", "Invalid HTTP Method")
        detail = error_info.get("detail", "Specified Method is invalid for this resource")
        raise PermissionError(f"Invalid HTTP Method: {title}. Detail: {detail}.")
    
    elif status_code == 406:     # Should only occur on certain functions
        error_info = response.json()
        title = error_info.get("title", "Wazuh Error")
        detail = error_info.get("The body type is not the one specified in the content-type")
        error_code = error_info.get("error", 6002)
        raise PermissionError(f"Wazuh Error: {title}. Detail: {detail}. Error Code: {error_code}.")
    
    elif status_code == 429:
        error_info = response.json()
        title = error_info.get("title", "Maximum Requests Per Minute Reached")
        detail = error_info.get("detail", "")
        remediation = error_info.get("remediation", "This limit can be changed in api.yaml file. More information here: https://documentation.wazuh.com/4.7/user-manual/api/security/configuration.html")
        error_code = error_info.get("error", 6001)
        raise PermissionError(f"Maximum requests per minute reached: {title}. Detail: {detail}. Error Code: {error_code}. Remediation: {remediation}")
    
    else:
        response.raise_for_status()  # Raise an HTTPError for other status codes, ie: error 500, 503
