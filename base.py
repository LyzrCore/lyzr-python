import requests
import json


class LyzrBaseClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "accept": "application/json",
            "x-api-key": self.api_key
        }

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            try:
                # Try to get a readable error message from the API response
                error_response = response.json()
                error_message = error_response.get("message") or str(error_response)
            except Exception:
                error_message = response.text  # Fallback to raw text if not JSON
            raise Exception(error_message)
        except Exception as e:
            raise Exception(e)

