import streamlit as st
from src.LanggraphAgenticai.ui.uiconfigfile import Config
import os

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        title = self.config.get_page_title()
        st.set_page_config(page_title=title, page_icon="🤖", layout="wide")
        st.header(f"🤖 {title}")
        st.divider()

        with st.sidebar:
            st.subheader("⚙️ Configuration")
            self.user_controls["selected_llm"] = st.selectbox("Select LLM Provider", self.config.get_llm_option())

            if self.user_controls["selected_llm"] == "Groq":
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", self.config.get_groq_model_option())
                self.user_controls["GROQ_API_KEY"] = st.text_input("API KEY", type="password", key="GROQ_API_KEY")
                
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ GROQ API KEY required to proceed.")
                    st.caption("Don't have one? Get it here: https://console.groq.com")

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", self.config.get_usecase_option())

            if self.user_controls["selected_usecase"] == "Chatbot With Web":
                tavily_key = st.text_input("TAVILY API KEY", type="password", key="TAVILY_API_KEY")
                self.user_controls["TAVILY_API_KEY"] = tavily_key

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please Enter Your Tavily Api Key To Proceed. Don't have? refer : https://app.tavily.com/home")


        return self.user_controls
