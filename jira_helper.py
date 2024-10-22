import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

load_dotenv()


url = f"{os.getenv('JIRA_URL')}/rest/api/3/issue"

def create_ticket(summary,description):
    auth = HTTPBasicAuth(os.getenv('JIRA_USER_NAME'), os.getenv('JIRA_API_KEY'))
    payload = json.dumps({
            "fields": {
                "project": {
                "key": "BTS"
                },
            "summary": summary,
            "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": description
                            }
                    ]
                    }
                    ]
                    },
            "issuetype": {
                    "name": "Bug"
                }
    }
    })
    headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
            }

    response = requests.request(
                "POST",
                url,
                data=payload,
                headers=headers,
                auth=auth
                )
    if response.status_code == 201:
        return True, response.json()
    else:
        return False, response.json()
