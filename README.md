# Pyzuh
Pyzuh is a python library for the Wazuh API. Inspired by Spotipy, Pyzuh's intend is to allow for easier use of the Wazuh API for tasks that range from adding agents to running logtests. I recommend that you read the Wazuh API for more under the hood and to familarize yourself with all the features. 

This can be found here: https://documentation.wazuh.com/current/user-manual/api/reference.html#section/Authentication

Note: This library is written based on the current version at the time (Version 4.7). This sunsets the vulnerability section on the API. 

# How does Pyzuh work? 
Wazuh uses jwt to make requests. Each request has 2-4 parts: header, body (if needed), parameters, and json (also if needed). Each function has a docstring you can view to get a better idea of what you will need to change for your specific needs. 

For example: 
```Python
from pyzuh import lists

help(lists.get_cdb_lists_files) # This will print the docstring for get_cdb_lists_files
```

The docstring for each function will help navigate what you want to change or state what will be required to fill into your requests for your own projects. 
