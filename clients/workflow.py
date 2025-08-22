from ..base import LyzrBaseClient


class LyzrWorkflows(LyzrBaseClient):
    """
    Client for Lyzr Agent API v3 - Workflows endpoints.
    """
    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url, api_key)

    def list_workflows(self):
        """
        List all workflows for the authenticated user.

        Returns:
        - List of workflows (list of dict).
        """
        endpoint = "/v3/workflows/"
        return self._request("GET", endpoint)

    def create_workflow(self, workflow_create_data: dict):
        """
        Create a new workflow.

        Args:
        - workflow_create_data: Data for creating a new workflow (dict).

        Returns:
        - workflow_response: The created workflow details (dict).
        """
        endpoint = "/v3/workflows/"
        return self._request("POST", endpoint, json=workflow_create_data)

    def get_workflow(self, flow_id: str):
        """
        Get a workflow by ID.

        Args:
        - flow_id: ID of the workflow (str).

        Returns:
        - workflow_response: The workflow details (dict).
        """
        endpoint = f"/v3/workflows/{flow_id}"
        return self._request("GET", endpoint)

    def update_workflow(self, flow_id: str, workflow_update_data: dict):
        """
        Update an existing workflow.

        Args:
        - flow_id: ID of the workflow (str).
        - workflow_update_data: Updated data for the workflow (dict).

        Returns:
        - workflow_response: The updated workflow details (dict).
        """
        endpoint = f"/v3/workflows/{flow_id}"
        return self._request("PUT", endpoint, json=workflow_update_data)

    def delete_workflow(self, flow_id: str):
        """
        Delete a workflow.

        Args:
        - flow_id: ID of the workflow (str).

        Returns:
        - None (status code 204 for successful deletion).
        """
        endpoint = f="/v3/workflows/{flow_id}"
        return self._request("DELETE", endpoint)

    def execute_workflow(self, flow_id: str, input_data: dict = None):
        """
        Execute a workflow with optional input data.

        Args:
        - flow_id: ID of the workflow (str).
        - input_data: Optional input data for the workflow (dict).

        Returns:
        - result: The result of the workflow execution (dict).
        """
        endpoint = f"/v3/workflows/{flow_id}/execute"
        return self._request("POST", endpoint, json=input_data)