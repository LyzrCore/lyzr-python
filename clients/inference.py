import requests
from ..base import LyzrBaseClient


class LyzrInference(LyzrBaseClient):
    """
    Client for Lyzr Agent API v3 - Inference endpoints.
    """
    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url, api_key)

    def chat(self, chat_request: dict):
        """
        Chat with an agent.

        Args:
        - chat_request: Details of the chat request (dict) including:
            - user_id (str): ID of the user.
            - agent_id (str): ID of the agent.
            - message (str): The message from the user.
            - session_id (Optional[str]): ID of the session.
            - system_prompt_variables (Optional[dict]): Variables for the system prompt.
            - filter_variables (Optional[dict]): Variables for filtering.
            - features (Optional[list]): List of features to use.

        Returns:
        - response: The agent's response (dict).
        """
        endpoint = "/v3/inference/chat/"
        return self._request("POST", endpoint, json=chat_request)

    def get_response(self, agent_id: str, request_body: dict):
        """
        Generate Response Endpoint

        Args:
        - agent_id: ID of the agent (str).
        - request_body: Request body containing messages and optional parameters (dict) including:
            - messages (list): List of message dictionaries.
            - response_format (Optional[str]): Desired format for the response.
            - run_id (Optional[str]): ID of the current run.
            - ops_metadata (Optional[dict]): Metadata for operations.

        Returns:
        - Response data (dict).
        """
        endpoint = f"/v3/inference/{agent_id}/generate_response/"
        return self._request("POST", endpoint, json=request_body)

    def task(self, chat_request: dict):
        """
        Create Chat Task

        Args:
        - chat_request: Details of the chat request (dict) including:
            - user_id (str): ID of the user.
            - agent_id (str): ID of the agent.
            - message (str): The message from the user.
            - session_id (Optional[str]): ID of the session.
            - system_prompt_variables (Optional[dict]): Variables for the system prompt.
            - filter_variables (Optional[dict]): Variables for filtering.
            - features (Optional[list]): List of features to use.

        Returns:
        - task_id: ID of the created task (dict).
        """
        endpoint = "/v3/inference/task/"
        return self._request("POST", endpoint, json=chat_request)

    def task_status(self, task_id: str):
        """
        Get Task Status

        Asynchronously retrieves the status of a task given its task ID.

        Args:
        - task_id: The unique identifier of the task (str).

        Returns:
        - Task status and result (dict) including:
            - task_id (str): The unique identifier of the task.
            - status (str): The status of the task.
            - result (Optional[dict]): The result of the task, if available.

        Possible statuses:
        - "pending": The task is still pending.
        - "failed": The task has failed, with an error message included in the result.
        - "completed": The task has successfully completed, with the result included.
        - "in_progress": The task is currently in progress.
        """
        endpoint = f"/v3/inference/task/{task_id}"
        return self._request("GET", endpoint)

    def stream_chat(self, chat_request: dict):
        """
        Stream chat with an agent.

        Args:
        - chat_request: Details of the chat request (dict) including:
            - user_id (str): ID of the user.
            - agent_id (str): ID of the agent.
            - message (str): The message from the user.
            - session_id (Optional[str]): ID of the session.
            - system_prompt_variables (Optional[dict]): Variables for the system prompt.
            - filter_variables (Optional[dict]): Variables for filtering.
            - features (Optional[list]): List of features to use.

        Returns:
        - response: The agent's response (stream).
        """
        # Note: Streaming requires different handling than a simple JSON response.
        # This implementation returns the raw requests Response object.
        # You would need to process response.iter_lines() or response.iter_content()
        # on the caller side for true streaming.
        endpoint = "/v3/inference/stream/"
        url = f"{self.base_url}{endpoint}"
        response = requests.request("POST", url, headers=self.headers, json=chat_request, stream=True)
        response.raise_for_status()
        return response # Return the raw response for streaming

    def create_webrtc_session(self, agent_id: str, voice_id: str):
        """
        Create a new WebRTC session for real-time audio/text interaction.
        Uses the agent's system prompt for instructions and returns the session details.

        Args:
        - agent_id: ID of the agent (str).
        - voice_id: ID of the voice to use (str).

        Returns:
        - WebRTC session details (dict).
        """
        endpoint = f"/v3/inference/webrtc-session/{agent_id}/{voice_id}"
        return self._request("POST", endpoint)