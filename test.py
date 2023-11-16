#!/usr/bin/env python
"""Example LangChain server exposes a conversational AI agent for summarization."""
from fastapi import FastAPI
from langchain.agents import AgentExecutor, tool
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.pydantic_v1 import BaseModel

from langserve import add_routes

@tool
def summarize_text(text: str) -> str:
    """Returns a summarized version of the given text."""
    # Implement summarization logic here, possibly using ChatOpenAI or another method
    summarized_text = "Summarized version of: " + text  # Placeholder implementation
    return summarized_text

tools = [summarize_text]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant capable of summarizing texts."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

llm = ChatOpenAI()

llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_functions(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIFunctionsAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tools)

app = FastAPI(
    title="LangChain Summarization Server",
    version="1.0",
    description="API server using Langchain's Runnable interfaces for text summarization",
)

class Input(BaseModel):
    input: str

class Output(BaseModel):
    output: str

add_routes(app, agent_executor.with_types(input_type=Input, output_type=Output))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
