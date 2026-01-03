import streamlit as st
import google.generativeai as genai

# Configure API key (consider using environment variables for production)
genai.configure(api_key="enter ur api key")

# Initialize the model
def setup_model():
    generation_config = {
        "temperature": 0.9,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
    
    return genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
    )

# Initialize Streamlit UI
st.set_page_config(page_title="Gemini AI Chatbot", page_icon="🤖")
st.title("🤖 Gemini AI Chatbot")
st.caption("A simple chatbot powered by Google's Gemini AI")

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = setup_model().start_chat(history=[])
    st.session_state.messages = [{"role": "ai", "content": "Hi! I'm your Gemini AI assistant. How can I help you today?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("ai"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
    
    # Add AI response to chat history

    st.session_state.messages.append({"role": "ai", "content": response.text})
