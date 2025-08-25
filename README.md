# Lyzr Python SDK

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lyzr-python-sdk)
![PyPI](https://img.shields.io/pypi/v/lyzr-python-sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python client library for interacting with the Lyzr Agent API. This SDK provides a convenient and structured way to access all Lyzr API functionalities, including managing agents, tools, providers, workflows, and handling inference requests.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [API Reference](#api-reference)
  - [Agents](#agents)
  - [Tools](#tools)
  - [Providers](#providers)
  - [Inference](#inference)
  - [Workflows](#workflows)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Installation

Install the package using pip:

```bash
pip install lyzr-python-sdk
```

## Quick Start

```python
from lyzr_python_sdk import LyzrAgentAPI
import os

# Initialize the client
api_key = os.environ.get("LYZR_AGENT_API_KEY")
client = LyzrAgentAPI(api_key=api_key)

# Get all agents
agents = client.agents.get_agents()
print(f"Found {len(agents)} agents")

# Chat with an agent
chat_response = client.inference.chat({
    "user_id": "user@example.com",
    "agent_id": "your-agent-id",
    "message": "Hello! How can you help me?",
    "session_id": "session-123"  # Optional for conversation continuity
})
print(chat_response)
```

## Authentication

The SDK requires a Lyzr API key for authentication. You can obtain your API key from the Lyzr dashboard.

```python
# Method 1: Environment variable (recommended)
import os
api_key = os.environ.get("LYZR_AGENT_API_KEY")
client = LyzrAgentAPI(api_key=api_key)

# Method 2: Direct initialization
client = LyzrAgentAPI(api_key="your-api-key-here")

## API Reference

### Agents

The `client.agents` provides methods to manage agents.

#### `get_agents()`
Get all agents associated with your API key.

```python
agents = client.agents.get_agents()
```

#### `create_agent(agent_config: dict)`
Create a new agent.

```python
agent_config = {
    "template_type": "single_task",
    "name": "My Assistant",
    "description": "A helpful AI assistant",
    "agent_role": "Assistant",
    "agent_instructions": "You are a helpful assistant that provides accurate information",
    "agent_goal": "Help users with their questions and tasks",
    "features": [],
    "tool": "",
    "tool_usage_description": "",
    "response_format": {
        "type": "text"
    },
    "provider_id": "OpenAI",
    "model": "gpt-4o",
    "top_p": "0.9",
    "temperature": "0.7",
    "managed_agents": [],
    "llm_credential_id": "lyzr_openai"
}
agent = client.agents.create_agent(agent_config)
```

#### `create_single_task_agent(agent_config: dict)`
Create a single-task agent using a template.

```python
agent_config = {
    "template_type": "single_task",
    "name": "Task Specialist",
    "description": "Specialized agent for specific tasks",
    "agent_role": "Specialist",
    "agent_instructions": "Focus on completing the assigned task efficiently",
    "agent_goal": "Complete specific tasks with high accuracy",
    "features": [],
    "tool": "",
    "tool_usage_description": "",
    "response_format": {
        "type": "text"
    },
    "provider_id": "OpenAI",
    "model": "gpt-4o",
    "top_p": "0.9",
    "temperature": "0.7",
    "managed_agents": [],
    "llm_credential_id": "lyzr_openai"
}
agent = client.agents.create_single_task_agent(agent_config)
```

#### `get_agent(agent_id: str)`
Get details of a specific agent.

```python
agent = client.agents.get_agent("agent-123")
```

#### `update_agent(agent_id: str, agent_config: dict)`
Update an existing agent.

```python
update_config = {
    "name": "Updated Assistant",
    "description": "An updated helpful AI assistant",
    "agent_role": "Senior Assistant",
    "agent_instructions": "You are an experienced assistant with enhanced capabilities",
    "agent_goal": "Provide comprehensive help with complex tasks",
    "features": [],
    "tool": "",
    "tool_usage_description": "",
    "response_format": {
        "type": "text"
    },
    "provider_id": "OpenAI",
    "model": "gpt-4o",
    "top_p": "0.8",
    "temperature": "0.5",
    "managed_agents": [],
    "llm_credential_id": "lyzr_openai"
}
result = client.agents.update_agent("agent-123", update_config)
```

#### `delete_agent(agent_id: str)`
Delete an agent.

```python
result = client.agents.delete_agent("agent-123")
```

#### `list_agent_versions(agent_id: str)`
List all versions of an agent.

```python
versions = client.agents.list_agent_versions("agent-123")
```

#### `get_agent_version(agent_id: str, version_id: str)`
Get a specific version of an agent.

```python
version = client.agents.get_agent_version("agent-123", "version_id")
```

#### `activate_agent_version(agent_id: str, version_id: str)`
Activate a specific agent version.

```python
result = client.agents.activate_agent_version("agent-123", "version_id")
```

#### `update_single_task_agent(agent_id: str, agent_config: dict)`
Update a single-task agent.

```python
update_config = {
    "name": "Updated Task Agent",
    "description": "Enhanced task-focused agent",
    "agent_role": "Task Expert",
    "agent_instructions": "You are an expert at handling specific tasks with precision",
    "agent_goal": "Execute tasks with maximum efficiency and accuracy",
    "features": [],
    "tool": "",
    "tool_usage_description": "",
    "response_format": {
        "type": "json"
    },
    "provider_id": "OpenAI",
    "model": "gpt-4o",
    "top_p": "0.9",
    "temperature": "0.3",
    "managed_agents": [],
    "llm_credential_id": "lyzr_openai"
}
result = client.agents.update_single_task_agent("agent-123", update_config)
```

### Tools

The `client.tools` provides methods to manage tools and integrations.

#### `get_tools()`
Get all tools for the user.

```python
tools = client.tools.get_tools()
```

#### `create_tool(tool_data: dict)`
Create a new tool from an OpenAPI schema.

```python
tool_data = {
    "tool_set_name": "my-api-tools",
    "openapi_schema": {...},  # Your OpenAPI schema
    "default_headers": {"Authorization": "Bearer token"},
    "enhance_descriptions": True
}
tool = client.tools.create_tool(tool_data)
```

#### `get_tool(tool_id: str)`
Get details of a specific tool.

```python
tool = client.tools.get_tool("tool-123")
```

#### `get_tool_info(tool_id: str)`
Get information about an OpenAPI tool.

```python
info = client.tools.get_tool_info("tool-123")
```

#### `toggle_tool(tool_id: str, enabled: bool)`
Enable or disable a tool.

```python
# Enable tool
result = client.tools.toggle_tool("tool-123", True)

# Disable tool
result = client.tools.toggle_tool("tool-123", False)
```

#### `delete_tool(tool_id: str)`
Delete a tool.

```python
result = client.tools.delete_tool("tool-123")
```

#### Composio Integration Methods

#### `get_composio_tools()`
Get available Composio tools.

```python
composio_tools = client.tools.get_composio_tools()
```


#### `get_composio_connected_accounts()`
Get connected Composio accounts.

```python
accounts = client.tools.get_composio_connected_accounts()
```

#### `delete_composio_connection(connection_id: str)`
Delete a Composio connection.

```python
result = client.tools.delete_composio_connection("conn-123")
```

### Providers

The `client.providers` provides methods to manage AI model providers and credentials.

#### `create_provider(provider_body: dict)`
Create a new provider.

```python
provider_body = {
    "vendor_id": "openai",
    "type": "llm",
    "form": {
        "api_key": "your-openai-key"
    }
}
provider = client.providers.create_provider(provider_body)
```

#### `create_lyzr_provider(provider_body: dict)`
Create a Lyzr provider.

```python
provider_body = {
    "type": "llm",
    "metadata": {
        "model": "gpt-4"
    }
}
provider = client.providers.create_lyzr_provider(provider_body)
```

#### `get_providers(provider_type: str)`
Get providers by type.

```python
llm_providers = client.providers.get_providers("llm")
```

#### `get_provider(provider_id: str)`
Get a specific provider.

```python
provider = client.providers.get_provider("provider-123")
```

#### `delete_provider(provider_id: str)`
Delete a provider.

```python
result = client.providers.delete_provider("provider-123")
```

#### Provider Credentials

#### `create_provider_credential(credential_data: dict)`
Create a provider credential.

```python
credential_data = {
    "provider_id": "provider-123",
    "name": "OpenAI Credential",
    "config": {"api_key": "sk-..."}
}
credential = client.providers.create_provider_credential(credential_data)
```

#### `create_bigquery_credential(credential_data: str, service_account_json_file_path: str)`
Create a BigQuery credential with service account file.

```python
credential_data = '{"project_id": "my-project"}'
credential = client.providers.create_bigquery_credential(
    credential_data,
    "/path/to/service-account.json"
)
```

#### `create_file_upload_credential(credential_data: str, files: list)`
Create a file upload credential.

```python
credential_data = '{"name": "File Upload"}'
files = ["/path/to/file1.txt", "/path/to/file2.pdf"]
credential = client.providers.create_file_upload_credential(credential_data, files)
```

#### `get_provider_credential(credential_id: str)`
Get a provider credential.

```python
credential = client.providers.get_provider_credential("cred-123")
```

#### `update_provider_credential(credential_id: str, update_data: dict)`
Update a provider credential.

```python
update_data = {
    "config": {"api_key": "new-key"}
}
result = client.providers.update_provider_credential("cred-123", update_data)
```

#### `delete_provider_credential(credential_id: str)`
Delete a provider credential.

```python
result = client.providers.delete_provider_credential("cred-123")
```

#### `get_all_credentials(provider_type: str, provider_id: str)`
Get all credentials for a provider.

```python
credentials = client.providers.get_all_credentials("llm", "provider-123")
```

#### `get_all_credentials_by_type(provider_type: str)`
Get all credentials by type.

```python
llm_credentials = client.providers.get_all_credentials_by_type("llm")
```

### Inference

The `client.inference` provides methods for AI inference and chat operations.

#### `chat(chat_request: dict)`
Chat with an agent.

```python
chat_request = {
    "user_id": "user@example.com",
    "agent_id": "agent-123",
    "message": "Hello, how can you help me?",
    "session_id": "session-456"
}
response = client.inference.chat(chat_request)
```

#### `get_response(agent_id: str, request_body: dict)`
Generate a response from an agent.

```python
request_body = {
    "messages": [
        {"role": "user", "content": "What is AI?"}
    ],
    "response_format": "json"  # Optional
}
response = client.inference.get_response("agent-123", request_body)
```

#### `task(chat_request: dict)`
Create a chat task (asynchronous).

```python
chat_request = {
    "user_id": "user@example.com",
    "agent_id": "agent-123",
    "message": "Hello, how can you help me?",
    "session_id": "session-456" 
}
task = client.inference.task(chat_request)
task_id = task["task_id"]
```

#### `task_status(task_id: str)`
Get the status of a task.

```python
status = client.inference.task_status("task-123")
print(f"Status: {status['status']}")
if status['status'] == 'completed':
    print(f"Result: {status['result']}")
```

#### `stream_chat(chat_request: dict)`
Stream chat with an agent (returns raw response for streaming).

```python
chat_request = {
    "user_id": "user@example.com",
    "agent_id": "agent-123",
    "message": "Hello, how can you help me?",
    "session_id": "session-456" 
}
response = client.inference.stream_chat(chat_request)

# Process streaming response
for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))
```

### Workflows

The `client.workflow` provides methods to manage and execute workflows.

#### `list_workflows()`
List all workflows.

```python
workflows = client.workflow.list_workflows()
```

#### `create_workflow(workflow_create_data: dict)`
Create a new workflow.

```python
workflow_data = {
    "name": "Data Processing Workflow",
    "description": "Process and analyze data",
    "steps": [
        {"type": "data_input", "config": {...}},
        {"type": "analysis", "config": {...}}
    ]
}
workflow = client.workflow.create_workflow(workflow_data)
```

#### `get_workflow(flow_id: str)`
Get a specific workflow.

```python
workflow = client.workflow.get_workflow("workflow-123")
```

#### `update_workflow(flow_id: str, workflow_update_data: dict)`
Update a workflow.

```python
update_data = {
    "name": "Updated Workflow Name",
    "description": "Updated description"
}
result = client.workflow.update_workflow("workflow-123", update_data)
```

#### `delete_workflow(flow_id: str)`
Delete a workflow.

```python
result = client.workflow.delete_workflow("workflow-123")
```

#### `execute_workflow(flow_id: str, input_data: dict)`
Execute a workflow.

```python
input_data = {
    "data_source": "file.csv",
    "parameters": {"threshold": 0.8}
}
result = client.workflow.execute_workflow("workflow-123", input_data)
```

## Examples

### Complete Agent Interaction Example

```python
from lyzr_python_sdk import LyzrAgentAPI
import os

# Initialize client
client = LyzrAgentAPI(api_key=os.environ.get("LYZR_AGENT_API_KEY"))

# Create an agent
agent_config = {
    "template_type": "single_task",
    "name": "Data Analyst",
    "description": "Expert data analysis assistant",
    "agent_role": "Data Analyst",
    "agent_instructions": "You are an expert data analyst who provides insights from data",
    "agent_goal": "Analyze data and provide actionable insights",
    "features": [],
    "tool": "",
    "tool_usage_description": "",
    "response_format": {
        "type": "text"
    },
    "provider_id": "OpenAI",
    "model": "gpt-4o",
    "top_p": "0.9",
    "temperature": "0.7",
    "managed_agents": [],
    "llm_credential_id": "lyzr_openai"
}
agent = client.agents.create_agent(agent_config)
agent_id = agent["agent_id"]

# Chat with the agent
chat_response = client.inference.chat({
    "user_id": "user@example.com",
    "agent_id": agent_id,
    "message": "Hello, how can you help me?",
    "session_id": "session-456" 
})

print(f"Agent response: {chat_response['response']}")

# Create and execute a task
task = client.inference.task({
    "user_id": "user@example.com",
    "agent_id": agent_id,
    "message": "Generate a comprehensive sales report for Q4",
    "session_id": "session-456" 
})

# Check task status
import time
while True:
    status = client.inference.task_status(task["task_id"])
    if status["status"] == "completed":
        print(f"Task completed: {status['result']}")
        break
    elif status["status"] == "failed":
        print(f"Task failed: {status['result']}")
        break
    time.sleep(2)
```

### Tool Integration Example

```python
# Create a tool from OpenAPI schema
tool_data = {
    "tool_set_name": "weather-api",
    "openapi_schema": {
        "openapi": "3.0.0",
        "info": {"title": "Weather API", "version": "1.0.0"},
        "paths": {
            "/weather": {
                "get": {
                    "summary": "Get weather data",
                    "parameters": [
                        {
                            "name": "city",
                            "in": "query",
                            "required": True,
                            "schema": {"type": "string"}
                        }
                    ]
                }
            }
        }
    },
    "default_headers": {"X-API-Key": "your-weather-api-key"}
}

tool = client.tools.create_tool(tool_data)
tool_id = tool["tool_ids"][0]

# Execute the tool
weather_data = client.tools.execute_tool(
    tool_id=tool_id,
    path="/weather",
    method="GET",
    params={"city": "New York"}
)

print(f"Weather data: {weather_data}")
```

## Error Handling

The SDK raises exceptions for API errors. Always wrap API calls in try-catch blocks:

```python
try:
    agents = client.agents.get_agents()
except Exception as e:
    print(f"Error fetching agents: {e}")
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [https://docs.lyzr.ai](https://docs.lyzr.ai)
- **GitHub Issues**: [https://github.com/LyzrCore/lyzr-python/issues](https://github.com/LyzrCore/lyzr-python/issues)
- **Email**: support@lyzr.ai

## Changelog

### v0.1.1
- Fixed package import structure
- Improved error handling
- Added comprehensive documentation

### v0.1.0
- Initial release
- Core API client functionality
- Support for Agents, Tools, Providers, Inference, and Workflows
