from ..base import LyzrBaseClient


class LyzrProviders(LyzrBaseClient):
    """
    Client for Lyzr Agent API v3 - Providers endpoints.
    """
    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url, api_key)

    def create_provider(self, provider_body: dict):
        """
        Create a new provider.

        Args:
        - provider_body: Contains `vendor_id`, `type`, and `form` details (dict).

        Returns:
        - The created provider with `createdAt` and `updatedAt` (dict).
        """
        endpoint = "/v3/providers/"
        return self._request("POST", endpoint, json=provider_body)

    def create_lyzr_provider(self, provider_body: dict):
        """
        Create a new Lyzr provider.

        Args:
        - provider_body: Contains `type`, and `metadata` details (dict).

        Returns:
        - The created provider with `createdAt` and `updatedAt` (dict).
        """
        endpoint = "/v3/providers/lyzr"
        return self._request("POST", endpoint, json=provider_body)

    def get_providers(self, provider_type: str):
        """
        Get all providers associated with a specific API key and provider type.

        Args:
        - provider_type: The type of provider to fetch (str).

        Returns:
        - A list of providers for the given API key and type (list).
        """
        endpoint = "/v3/providers/type"
        params = {"provider_type": provider_type}
        return self._request("GET", endpoint, params=params)

    def get_provider(self, provider_id: str):
        """
        Get provider associated with a specific provider ID.

        Args:
        - provider_id: The provider ID to fetch provider for (str).

        Returns:
        - A provider for the given provider ID (dict).
        """
        endpoint = f"/v3/providers/{provider_id}"
        return self._request("GET", endpoint)

    def update_provider(self, provider_id: str, update_data: dict):
        """
        Update an existing provider.

        Args:
        - provider_id: The ID of the provider to update (str).
        - update_data: Contains updated `type` and `form` details (dict).

        Returns:
        - The updated provider (dict).
        """
        endpoint = f"/v3/providers/{provider_id}"
        return self._request("PUT", endpoint, json=update_data)

    def delete_provider(self, provider_id: str):
        """
        Delete a provider by ID.

        Args:
        - provider_id: The ID of the provider to delete (str).

        Returns:
        - A message confirming the provider was deleted (dict).
        """
        endpoint = f"/v3/providers/{provider_id}"
        return self._request("DELETE", endpoint)

    def create_provider_credential(self, credential_data: dict):
        """
        Create a new provider credential.

        Args:
        - credential_data: The data required to create a credential (dict).

        Returns:
        - A message confirming the credential was created, and the credential ID (dict).
        """
        endpoint = "/v3/providers/credentials"
        return self._request("POST", endpoint, json=credential_data)

    def create_bigquery_credential(self, credential_data: str, service_account_json_file_path: str):
        """
        Create a new BigQuery provider credential.

        Args:
        - credential_data: The data required to create a credential (JSON string).
        - service_account_json_file_path: Path to the service account JSON file (str).

        Returns:
        - A message confirming the credential was created, and the credential ID (dict).
        """
        endpoint = "/v3/providers/credentials/big_query"
        files = {'service_account_json': open(service_account_json_file_path, 'rb')}
        data = {'credential_data': credential_data}
        return self._request("POST", endpoint, data=data, files=files)

    def create_file_upload_credential(self, credential_data: str, files: list):
        """
        Create a new file upload credential.

        Args:
        - credential_data: The data required to create a credential (JSON string).
        - files: A list of file paths to upload (list of str).

        Returns:
        - A message confirming the credential was created, and the credential ID (dict).
        """
        endpoint = "/v3/providers/credentials/file_upload"
        file_list = [('files', (f, open(f, 'rb'))) for f in files]
        data = {'credential_data': credential_data}
        return self._request("POST", endpoint, data=data, files=file_list)

    def get_provider_credential(self, credential_id: str):
        """
        Get a provider credential by its ID.

        Args:
        - credential_id: The credential ID to fetch the provider credential for (str).

        Returns:
        - The provider credential data (dict).
        """
        endpoint = f"/v3/providers/credentials/{credential_id}"
        return self._request("GET", endpoint)

    def update_provider_credential(self, credential_id: str, update_data: dict):
        """
        Update a provider credential by its ID.

        Args:
        - credential_id: The credential ID to update the provider credential for (str).
        - update_data: The updated data for the credential (dict).

        Returns:
        - A message confirming the credential was updated (dict).
        """
        endpoint = f"/v3/providers/credentials/{credential_id}"
        return self._request("PUT", endpoint, json=update_data)

    def update_file_upload_credential(self, credential_id: str, update_data: str, files: list = None):
        """
        Update a file upload credential.

        Args:
        - credential_id: The credential ID to update the file upload credential for (str).
        - update_data: The updated data for the credential (JSON string).
        - files: An optional list of new file paths to upload (list of str).

        Returns:
        - A message confirming the credential was updated (dict).
        """
        endpoint = f"/v3/providers/credentials/file_upload/{credential_id}"
        file_list = None
        if files:
            file_list = [('files', (f, open(f, 'rb'))) for f in files]
        data = {'update_data': update_data}
        return self._request("PUT", endpoint, data=data, files=file_list)


    def delete_provider_credential(self, credential_id: str):
        """
        Delete a provider credential by its ID.

        Args:
        - credential_id: The credential ID to delete (str).

        Returns:
        - A message confirming the credential was deleted (dict).
        """
        endpoint = f"/v3/providers/credentials/{credential_id}"
        return self._request("DELETE", endpoint)

    def get_all_credentials(self, provider_type: str, provider_id: str):
        """
        Get all provider credentials by user and provider type and provider Id.

        Args:
        - provider_type: The type of provider credential to fetch (str).
        - provider_id: The id of provider credential to fetch (str).

        Returns:
        - A list of provider credentials (list).
        """
        endpoint = f"/v3/providers/credentials/user/{provider_type}/{provider_id}"
        return self._request("GET", endpoint)

    def get_all_credentials_by_type(self, provider_type: str):
        """
        Get all provider credentials by type and user id.

        Args:
        - provider_type: The type of provider credential to fetch (str).

        Returns:
        - A list of provider credentials of the specified type (list).
        """
        endpoint = f"/v3/providers/credentials/type/{provider_type}"
        return self._request("GET", endpoint)