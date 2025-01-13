from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    ManagedAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel,
)
from visit_webpage_tool import visit_webpage


# Configure the model using Ollama, note that the api key for local models can be any text, I use 'ollama' here
model = LiteLLMModel(model_id="ollama_chat/qwen2.5-coder:7b-instruct-q8_0", api_key="ollama")

# Create the tool calling agent that calls the DuckDuckGo search tool and the visit webpage tool
web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage],
    model=model,
    max_steps=10,  # Set the maximum number of steps to 10 to search at most 10 pages
)

# Create the managed agent that manages the web agent callable
managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="search",
    description="Runs web searches for you. Give it your query as an argument.",
)

# Create the manager agent tasked with planning and thinking, advanced reasoning, etc.
# CodeAgent is used here as its the most powerful agent type from smolagents for these requirements
manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[managed_web_agent],
    additional_authorized_imports=["time", "numpy", "pandas"], # Add packages in case the agent needs to make calculations
)

# Run the agent
answer = manager_agent.run(
    "If LLM training continues to scale up at the current rhythm until 2030, "
    "what would be the electric power in GW required to power the biggest training runs by 2030? "
    "What would that correspond to, compared to some countries? Please provide a source for any numbers used."
)
