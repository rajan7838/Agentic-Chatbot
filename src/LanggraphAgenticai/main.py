import streamlit as st
from src.LanggraphAgenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.LanggraphAgenticai.LLM.groqllm import GroqLLM
from src.LanggraphAgenticai.graph.graph_builder import GraphBuilder
from src.LanggraphAgenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Initialises and displays the Streamlit user interface for the LangGraph Agentic AI application.

    This function instantiates the UI loader, renders the sidebar configuration controls 
    (LLM selection, Groq models, API keys, and use cases), and captures user inputs to 
    drive the stateful execution graph.

    Returns:
        dict: A dictionary containing the user's selected UI controls and configuration state.
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("ERROR: Failed to load user input from the UI")
        return

    user_message = st.chat_input("Enter your messages: ")

    if user_message:
        try:
            #configure the llm
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_models()


            if not model:
                st.error("Error: LLm model could not be initialized")
                return

            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No use case selected")
                return

            graph_builder =  GraphBuilder(model,tavily_api_key=user_input.get("TAVILY_API_KEY"))

            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: graph setup failed : {e}") 
                return   

        except Exception as e:
            st.error(f"Error: graph setup failed : {e}") 
            return 
