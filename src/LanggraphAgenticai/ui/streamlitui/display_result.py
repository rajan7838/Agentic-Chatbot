import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        
    def display_result_on_ui(self):
        if self.usecase not in ["Basic Chatbot", "Chatbot With Web"]:
            st.warning(f"Usecase '{self.usecase}' not implemented yet.")
            return

        # User message ek baar dikhao
        with st.chat_message("user"):
            st.write(self.user_message)

        # Graph ko stream karo
        for event in self.graph.stream({"messages": [HumanMessage(content=self.user_message)]}):
            for value in event.values():
                messages = value.get("messages")
                
                # Check karo list hai ya single object, aur sirf AI response dikhao
                if isinstance(messages, list):
                    for msg in messages:
                        if isinstance(msg, AIMessage) and msg.content:
                            with st.chat_message("assistant"):
                                st.write(msg.content)
                elif isinstance(messages, AIMessage) and messages.content:
                    with st.chat_message("assistant"):
                        st.write(messages.content)