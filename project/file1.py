import streamlit as st
import time
import random
import threading

# Simulated AI suggestions
AI_SUGGESTIONS = [
    "Consider using a list comprehension here.",
    "This loop could be optimized using enumerate().",
    "Don't forget to add error handling for this function.",
    "You might want to consider breaking this into smaller functions.",
    "Remember to add docstrings to your functions.",
]

def get_ai_suggestion():
    """Simulate AI generating a suggestion."""
    return random.choice(AI_SUGGESTIONS)

def ai_assistant():
    """Continuously update AI suggestions."""
    while True:
        time.sleep(5)  # Check every 5 seconds
        if st.session_state.code.strip():
            st.session_state.ai_suggestion = get_ai_suggestion()
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage

def main():
    st.title("AI-Enhanced Code Collaboration Tool")

    # Initialize session state
    if 'code' not in st.session_state:
        st.session_state.code = ""
    if 'ai_suggestion' not in st.session_state:
        st.session_state.ai_suggestion = ""

    # Start AI assistant thread
    if 'ai_thread' not in st.session_state:
        st.session_state.ai_thread = threading.Thread(target=ai_assistant)
        st.session_state.ai_thread.daemon = True
        st.session_state.ai_thread.start()

    # Code Editor
    st.subheader("Code Editor")
    st.session_state.code = st.text_area("Write your code here:", value=st.session_state.code, height=300, key="code_editor")

    # AI Suggestions
    st.subheader("AI Assistant")
    suggestion_placeholder = st.empty()

    # Update AI suggestion
    if st.session_state.ai_suggestion:
        suggestion_placeholder.info(f"AI Assistant: {st.session_state.ai_suggestion}")

    # Simulate real-time updates
    st.empty()

if __name__ == "__main__":
    main()