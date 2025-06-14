from langchain.agents import initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
import os

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tools = load_tools(["llm-math"], llm)

agent = initialize_agent(
    tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)
