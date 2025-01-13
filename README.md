# Agentic AI Playground

An Agentic AI Research Assistant multi-agent system leveraging the smolagent library. Models used to run agents locally include llama3.1:8b-instruct-q8_0, llama3.1:8b-q8_0, qwen2.5:7b-instruct-q8_0, and qwen2.5-coder:7b-instruct-q8_0

## Notes

- When running agents locally that use the `smolagents` library, ensure that you are using a coding optimized LLM for optimized performance given that `smolagents` lets the agents write actual Python code to perform their actions, which means a strong coding model is needed to ensure that the agents can write good code. Locally, I usually run `qwen2.5-coder:7b-instruct-q8_0` for the best performance.
