# Pyzuh
Pyzuh is a python library for the Wazuh API. Inspired by Spotipy, Pyzuh's intend is to allow for easier use of the Wazuh API for tasks that range from adding agents to running logtests. I recommend that you read the Wazuh API for more under the hood and to familarize yourself with all the features. 

This can be found here: https://documentation.wazuh.com/current/user-manual/api/reference.html#section/Authentication

Note: This library is written based on the current version at the time (Version 4.7). This sunsets the vulnerability section on the API. 

## How does Pyzuh work? 
Wazuh (and thus Pyzuh) uses jwt to make requests. Each request has 2-4 parts: header, body (if needed), parameters, and json (also if needed). Each function has a docstring you can view to get a better idea of what you will need to change for your specific needs. 

For example: 
```Python
from pyzuh import lists

help(lists.get_cdb_lists_files) # This will print the docstring for get_cdb_lists_files
```

The docstring for each function will help navigate what you want to change or state what will be required to fill into your requests for your own projects. 

## Installation 
```
pip install pyzuh
```
For Windows Users: 
```
py -m pip install pyzuh
```
## Examples
I have included an examples folder where you can use some basic ideas as a starting point or use the code for your own SOC deployments. Here is a basic example of a project idea where you run a scan and it post to a slack channel: 
```Python
from pyzuh import Agents
import json

def run_scan_and_post_to_slack(wazuh_client, slack_webhook_url):
    # Run system scan on all agents
    response = wazuh_client.run_sysscan(pretty=True, wait_for_complete=True)

    # Post response to Slack channel
    slack_message = {
        "text": "Wazuh system scan completed",
        "attachments": [
            {
                "text": json.dumps(response, indent=4)
            }
        ]
    }
    requests.post(slack_webhook_url, json=slack_message)

if __name__ == "__main__":
    # Initialize the Wazuh client
    wazuh_client = Agents(api_url='your-wazuh-api-url', jwt_token='your-wazuh-jwt-token')

    # Define your Slack webhook URL
    slack_webhook_url = 'your-slack-webhook-url'

    # Run system scan and post results to Slack
    run_scan_and_post_to_slack(wazuh_client, slack_webhook_url)
```
## Questions/Issues 
If you have run into any issues, file an issue or email me at austin@liliumsecurity.com.

FAQ can be found here:  <a href="https://github.com/Lilium48/Pyzuh/blob/main/docs/faq.md">FAQ</a>

