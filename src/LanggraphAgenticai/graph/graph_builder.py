from langgraph.graph import StateGraph,START,END
from src.LanggraphAgenticai.state.state import State
from src.LanggraphAgenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.LanggraphAgenticai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode
from src.LanggraphAgenticai.nodes.chatbot_with_tools_node import Chatbotwithtoolnode


class GraphBuilder:
    def __init__(self,model,tavily_api_key=None):
        self.llm = model
        self.graph_builder = StateGraph(State)
        self.tavily_api_key = tavily_api_key


    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class
        and integrates it into the graph. The chatbot node is set as both the
        entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_graph(self):
            """
            Builds an advanced chatbot graph with tool integration.
            This method creates a chatbot graph that includes both a chatbot node
            and a tool node. It defines tools, initializes the chatbot with tool
            capabilities, and sets up conditional and direct edges between nodes.
            The chatbot node is set as the entry point.
            """

            tools = get_tools(self.tavily_api_key)
            tool_node = create_tool_node(tools)

            llm = self.llm

            obj_chatbot_with_node = Chatbotwithtoolnode(llm)
            Chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

            self.graph_builder.add_node("chatbot",Chatbot_node)
            self.graph_builder.add_node("tools",tool_node)
            self.graph_builder.add_edge(START,"chatbot")
            self.graph_builder.add_conditional_edges("chatbot",tools_condition)
            self.graph_builder.add_edge("tools","chatbot")
            

            
          


    def setup_graph(self,usecase:str):
        """sets up the graph for the selected use case"""
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot With Web":
            self.chatbot_with_tools_graph()  

        return self.graph_builder.compile()    
        