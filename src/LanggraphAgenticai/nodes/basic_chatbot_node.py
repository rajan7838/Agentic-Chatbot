from src.LanggraphAgenticai.state.state import State


class BasicChatbotNode:
    """Basic chatbot login impliementation"""

    def __init__(self,model):
        self.llm = model


    def process(self,state:State)->dict :
        """Processes the input and a chatbot response"""

        return {"messages":self.llm.invoke(state['messages'])}   