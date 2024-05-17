from pyzuh import Agents
import requests
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
