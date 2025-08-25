__version__ = "0.1.5"

from .base import LyzrBaseClient
from .clients import (
    LyzrAgent,
    LyzrProviders,
    LyzrTools,
    LyzrInference,
    LyzrWorkflows
)


class LyzrAgentAPI(LyzrBaseClient):
    """
    A unified client for the Lyzr Agent API, providing access to various API sections.
    """
    def __init__(self, api_key: str, base_url: str = "https://agent-prod.studio.lyzr.ai"):
        """
        Initializes the Lyzr Agent API Client.

        Args:
            api_key (str): Your Lyzr Agent API key.
            base_url (str): The base URL for the Lyzr Agent API (defaults to production).
        """
        super().__init__(base_url, api_key)

        # Initialize clients for each API section
        self.agents = LyzrAgent(base_url, api_key)
        self.providers = LyzrProviders(base_url, api_key)
        self.tools = LyzrTools(base_url, api_key)
        self.inference = LyzrInference(base_url, api_key)
        self.workflow = LyzrWorkflows(base_url, api_key)


# Optional: Expose the main client class for direct import
__all__ = ["LyzrAgentAPI", "__version__"]