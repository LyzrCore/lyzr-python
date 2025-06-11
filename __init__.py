from .base import LyzrBaseClient
from .clients import (
    LyzrAgent,
    LyzrProviders,
    LyzrTools,
    LyzrInference
)


class LyzrAgentAPIClient(LyzrBaseClient):
    """
    A unified client for the Lyzr Agent API, providing access to various API sections.
    """
    def __init__(self, api_key: str, base_url: str = "https://agent-prod.studio.lyzr.ai/"):
        """
        Initializes the Lyzr Agent API Client.

        Args:
            api_key (str): Your Lyzr Agent API key.
            base_url (str): The base URL for the Lyzr Agent API (defaults to production).
        """
        super().__init__(base_url, api_key)

        # Initialize clients for each API section
        self.agents_v3 = LyzrAgent(base_url, api_key)
        self.providers_v3 = LyzrProviders(base_url, api_key)
        self.tools_v3 = LyzrTools(base_url, api_key)
        self.inference_v3 = LyzrInference(base_url, api_key)


# Optional: Expose the main client class for direct import
__all__ = ["LyzrAgentAPIClient"]