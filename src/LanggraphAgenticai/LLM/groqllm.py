import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_models(self):
        try:
            # 1. Fetching inputs safely
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "").strip()    
            selected_groq_model = self.user_controls_input.get("selected_groq_model")

            # 2. Checking if API Key is missing everywhere
            if not groq_api_key and not os.environ.get("GROQ_API_KEY"):
                st.error("⚠️ Please Enter The GROQ API KEY in the sidebar to proceed.")
                return None

            # 3. Initializing LLM outside the validation block
            llm = ChatGroq(
                api_key=groq_api_key or os.environ.get("GROQ_API_KEY"), 
                model=selected_groq_model
            )
            return llm

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception: {e}")
