from ..base import LyzrBaseClient


class LyzrTools(LyzrBaseClient):
    """
    Client for Lyzr Agent API v3 - Tools endpoints.
    """
    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url, api_key)

    def get_tools(self):
        """
        Get All Tools For An User

        Returns:
        - List of tools (dict).
        """
        endpoint = "/v3/tools/"
        return self._request("GET", endpoint)

    def create_tool(self, tool_data: dict):
        """
        Create a new tool from an OpenAPI schema with custom name and default parameters.

        Args:
        - tool_data: The OpenAPI tool creation data (dict) including:
            - tool_set_name (str): Name for the tool set (will be prefixed with 'openapi-')
            - openapi_schema (dict): The OpenAPI schema
            - default_headers (Optional[dict]): Optional default headers
            - default_query_params (Optional[dict]): Optional default query parameters
            - default_body_params (Optional[dict]): Optional default body parameters
            - endpoint_defaults (Optional[dict]): Optional endpoint-specific default parameters
            - enhance_descriptions (Optional[bool]): Whether to enhance endpoint descriptions
            - openai_api_key (Optional[str]): OpenAI API key for description enhancement

        Returns:
        - tool_ids: IDs of the created tools (dict).
        """
        endpoint = "/v3/tools/"
        return self._request("POST", endpoint, json=tool_data)

    def get_tool_info(self, tool_id: str):
        """
        Get information about an OpenAPI tool.

        Args:
        - tool_id: The ID of the tool to retrieve (str).

        Returns:
        - Tool information including paths and methods (dict).
        """
        endpoint = f"/v3/tools/openapi/{tool_id}"
        return self._request("GET", endpoint)

    def execute_tool(self, tool_id: str, path: str, method: str, params: dict = None):
        """
        Execute an OpenAPI tool with the given parameters.

        Args:
        - tool_id: The ID of the tool to execute (str).
        - path: The API path to call (str).
        - method: The HTTP method to use (str).
        - params: The parameters to pass to the tool (dict).

        Returns:
        - The result of the tool execution (dict).
        """
        endpoint = f"/v3/tools/openapi/{tool_id}/execute"
        query_params = {"path": path, "method": method}
        return self._request("POST", endpoint, params=query_params, json=params)

    def get_tool(self, tool_id: str):
        """
        Get Tool Endpoint

        Args:
        - tool_id: The ID of the tool (str).

        Returns:
        - Tool details (dict).
        """
        endpoint = f"/v3/tools/{tool_id}"
        return self._request("GET", endpoint)

    def toggle_tool(self, tool_id: str, enabled: bool):
        """
        Enable/Disable a tool.

        Args:
        - tool_id: The ID of the tool (str).
        - enabled: Whether tool should be enabled or disabled (bool).

        Returns:
        - A message confirming the tool was updated (dict).
        """
        endpoint = f"/v3/tools/{tool_id}"
        params = {"enabled": enabled}
        return self._request("PATCH", endpoint, params=params)

    def delete_tool(self, tool_id: str):
        """
        Delete a tool.

        Args:
        - tool_id: The ID of the tool to delete (str).

        Returns:
        - A message confirming the tool was deleted (dict).
        """
        endpoint = f"/v3/tools/{tool_id}"
        return self._request("DELETE", endpoint)

    def update_tool(self, tool_id: str, update_data: dict):
        """
        Update a tool's configuration.

        Args:
        - tool_id: The ID of the tool to update (str).
        - update_data: Dictionary containing the fields to update (dict).

        Returns:
        - A message confirming the tool was updated (dict).
        """
        endpoint = f"/v3/tools/{tool_id}"
        return self._request("PUT", endpoint, json=update_data)

    def create_tool_credential(self, credential_data: dict):
        """
        Create a new Tool credential.

        Args:
        - credential_data: The data required to create a credential (dict).

        Returns:
        - A message confirming the credential was created (dict).
        """
        endpoint = "/v3/tools/credentials"
        return self._request("POST", endpoint, json=credential_data)

    def update_tool_credential(self, credential_id: str, update_data: dict):
        """
        Update a provider credential by its ID.

        Args:
        - credential_id: The credential ID to update the tool credential for (str).
        - update_data: The updated data for the credential (dict).

        Returns:
        - A message confirming the credential was updated (dict).
        """
        endpoint = f"/v3/tools/credentials/{credential_id}"
        return self._request("PUT", endpoint, json=update_data)

    def get_composio_tools(self):
        """
        Get Composio Tools

        Returns:
        - List of Composio tools (dict).
        """
        endpoint = "/v3/tools/composio/user"
        return self._request("GET", endpoint)

    def connect_composio_tool(self, app: str, redirect_url: str = "https://www.google.com"):
        """
        Connect Composio Tool

        Args:
        - app: The name of the application to connect (str).
        - redirect_url: The URL to redirect to after connection (str, default: "https://www.google.com").

        Returns:
        - Connection information (dict).
        """
        endpoint = f"/v3/tools/composio/connect/{app}"
        params = {"redirect_url": redirect_url}
        return self._request("GET", endpoint, params=params)

    def connect_composio_tool_with_params(self, app: str, collected_params: dict):
        """
        Connect Composio Tool With Params

        Args:
        - app: The name of the application to connect (str).
        - collected_params: Additional parameters for the connection (dict).

        Returns:
        - Connection information (dict).
        """
        endpoint = f"/v3/tools/composio/connect/{app}"
        return self._request("POST", endpoint, json=collected_params)

    def get_composio_connected_accounts(self):
        """
        Get connected accounts from Composio API.

        Returns:
        - List of active connected accounts with their ID and appUniqueId (dict).
        """
        endpoint = "/v3/tools/composio/connections"
        return self._request("GET", endpoint)

    def delete_composio_connection(self, connection_id: str):
        """
        Delete a connected account from Composio API.

        Args:
        - connection_id: The ID of the connected account to delete (str).

        Returns:
        - A message confirming the connection was deleted (dict).
        """
        endpoint = f"/v3/tools/composio/connections/{connection_id}"
        return self._request("DELETE", endpoint)