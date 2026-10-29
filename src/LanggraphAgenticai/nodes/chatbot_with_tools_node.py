from src.LanggraphAgenticai.state.state import State
from langchain_core.messages import HumanMessage

class Chatbotwithtoolnode:
    """Chatbot logic enhanced with tool integration"""

    def __init__(self, model):
        self.llm = model

    # process() method hata diya gaya hai kyunki wo buggy tha aur use nahi ho raha

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node