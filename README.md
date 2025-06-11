# Lyzr Agent API Python Client

![PyPI - Python Version](https://img.shields.io/pypi/py/lyzr-agent-api)
![PyPI](https://img.shields.io/pypi/v/lyzr-agent-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python client library for interacting with the Lyzr Agent API. This client provides a convenient and structured way to access the various functionalities offered by the API, including managing environments, agents, tools, handling inference requests, and interacting with user data and workflows.

## Table of Contents

*   [Description](#description)
*   [Installation](#installation)
*   [Quick Start](#quick-start)
*   [API Sections](#api-sections)
    *   [Agents (v3)](#agents-v3)
    *   [Providers (v3)](#providers-v3)
    *   [Tools (v3)](#tools-v3)
    *   [Inference (v3)](#inference-v3)
    *   [Semantic Model (v3)](#semantic-model-v3)
    *   [Users (v1)](#users-v1)
    *   [Workflows (v3)](#workflows-v3)
    *   [Ops (v3)](#ops-v3)
*   [Authentication](#authentication)
*   [Error Handling](#error-handling)
*   [Contributing](#contributing)
*   [License](#license)

## Description

The Lyzr Agent API is a modular, universal agent framework designed to simplify the creation of LLM-based agents. This Python client library aims to provide a seamless Python interface to interact with the API, abstracting away the HTTP request details and providing dedicated client objects for each major API section.

The framework's architecture is divided into three main components:

*   **Environment:** Defines the modules, features, available tools, and other configurations for your agent.
*   **Agent:** Specifies your agent's configuration, including the system prompt, name, and persona. The agent operates within an environment identified by an environment ID.
*   **Inference:** Handles the processing and execution of tasks and conversations.

This client library provides specific client classes for different API versions and functionalities, organized for clarity and ease of use.

## Installation

You can install the package using pip:

```bash
pip install lyzr-agent-api
```

### Quick Start
Here's a basic example demonstrating how to initialize the client and make a simple API call:

```python
from lyzr_agent_api import LyzrAgentAPIClient
import os

# Replace with your actual API key.
# It's recommended to use environment variables for sensitive information.
api_key = os.environ.get("LYZR_AGENT_API_KEY")
if not api_key:
    raise ValueError("LYZR_AGENT_API_KEY environment variable not set.")

try:
    # Initialize the main client
    client = LyzrAgentAPIClient(api_key=api_key)

    # Access a specific API section (e.g., Agents V3)
    print("Fetching agents...")
    agents = client.agents_v3.get_agents_by_api_key()
    print("All Agents:", agents)

except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Contributing
We welcome contributions to this Python client library! If you find a bug, have a feature request, or want to improve the documentation, please open an issue or submit a pull request on the GitHub repository.

- Fork the repository.
- Create a new branch for your feature or bugfix.
- Make your changes and write tests.
- Ensure tests pass.
- Submit a pull request.