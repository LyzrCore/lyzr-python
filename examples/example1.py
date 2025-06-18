from lyzr_python import LyzrAgentAPI

# Replace with your actual API key
# Optional, defaults to this

client = LyzrAgentAPI("enter your Lyzr API KEY here")

# Accessing Agents V3 endpoints
try:
    agents = client.agents.get_agents()
    print("All Agents:", len(agents))
except Exception as e:
    print(f"Error getting agents: {e}")

# Accessing Tools V3 endpoints
try:
    user_tools = client.tools.get_tools()
    print("User Tools:", len(user_tools))
except Exception as e:
    print(f"Error getting user tools: {e}")

# Accessing Inference V3 endpoints
try:
    chat_request_data = {
        "user_id": "demo@example.com",
        "agent_id": "68396a2dfee888", # Replace with actual agent ID
        "session_id": "asd", # Optional
        "message": "Hello! whats your role?"
    }
    chat_response = client.inference.chat(chat_request_data)
    print("Chat Response:", chat_response)
except Exception as e:
    print(f"Error chatting with agent: {e}")