from ..base import LyzrBaseClient


class LyzrAgent(LyzrBaseClient):
    """
    Client for Lyzr Agent API v3 - Agents endpoints.
    """
    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url, api_key)

    def get_agents(self):
        """
        Get all agents by API key.

        Returns:
        - agents: A list of agents associated with the given API key.
        """
        endpoint = "/v3/agents/"
        return self._request("GET", endpoint)

    def create_agent(self, agent_config: dict):
        """
        Create a new agent.

        Args:
        - agent_config: Configuration details for the agent (dict).

        Returns:
        - agent_id: ID of the created agent.
        """
        endpoint = "/v3/agents/"
        return self._request("POST", endpoint, json=agent_config)

    def create_single_task_agent(self, agent_config: dict):
        """
        Create a new single task agent.

        Args:
        - agent_config: Configuration details for the agent (dict).

        Returns:
        - agent_id: ID of the created agent.
        """
        endpoint = "/v3/agents/template/single-task"
        return self._request("POST", endpoint, json=agent_config)

    def update_agent(self, agent_id: str, agent_config: dict):
        """
        Update an existing agent.

        Args:
        - agent_id: ID of the agent to update (str).
        - agent_config: Configuration details for the agent (dict).

        Returns:
        - message: Success message after update (dict).
        """
        endpoint = f"/v3/agents/{agent_id}"
        return self._request("PUT", endpoint, json=agent_config)

    def delete_agent(self, agent_id: str):
        """
        Delete an agent by ID.

        Args:
        - agent_id: ID of the agent to delete (str).

        Returns:
        - message: Success message after deletion (dict).
        """
        endpoint = f"/v3/agents/{agent_id}"
        return self._request("DELETE", endpoint)

    def get_agent(self, agent_id: str):
        """
        Get agent details by ID.

        Args:
        - agent_id: ID of the agent to retrieve (str).

        Returns:
        - agent: The agent data (dict).
        """
        endpoint = f"/v3/agents/{agent_id}"
        return self._request("GET", endpoint)

    def list_agent_versions(self, agent_id: str):
        """
        List the versions of an agent.

        Args:
        - agent_id: ID of the agent (str).

        Returns:
        - versions: A list of agent versions (dict).
        """
        endpoint = f"/v3/agents/{agent_id}/versions"
        return self._request("GET", endpoint)

    def get_agent_version(self, agent_id: str, version_id: str):
        """
        Get a specific version of an agent.

        Args:
        - agent_id: ID of the agent (str).
        - version_id: ID of the version (str).

        Returns:
        - version_data: The agent version data (dict).
        """
        endpoint = f"/v3/agents/{agent_id}/versions/{version_id}"
        return self._request("GET", endpoint)

    def activate_agent_version(self, agent_id: str, version_id: str):
        """
        Activate an agent version.

        Args:
        - agent_id: ID of the agent (str).
        - version_id: ID of the version (str).

        Returns:
        - message: Success message after activation (dict).
        """
        endpoint = f"/v3/agents/{agent_id}/versions/{version_id}/activate"
        return self._request("POST", endpoint)

    def update_single_task_agent(self, agent_id: str, agent_config: dict):
        """
        Update an existing single task agent.

        Args:
        - agent_id: ID of the agent to update (str).
        - agent_config: Configuration details for the agent (dict).

        Returns:
        - message: Success message after update (dict).
        """
        endpoint = f="/v3/agents/template/single-task/{agent_id}"
        return self._request("PUT", endpoint, json=agent_config)