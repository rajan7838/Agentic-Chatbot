from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools(tavily_api_key: str):
    """Return the list of tools to be used in the chatbot"""

    return [TavilySearchResults(tavily_api_key=tavily_api_key, max_results=2)]

def create_tool_node(tools):
    """create and return a tool node fro the graph"""

    return ToolNode(tools=tools)