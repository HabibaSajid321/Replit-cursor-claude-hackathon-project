import streamlit as st
import requests
import json
import random

# Simulated AI suggestions
AI_SUGGESTIONS = [
    "Consider using a list comprehension here.",
    "This loop could be optimized using enumerate().",
    "Don't forget to add error handling for this function.",
    "You might want to consider breaking this into smaller functions.",
    "Remember to add docstrings to your functions.",
]

# Replit API endpoint (replace with actual endpoint when available)
REPLIT_API_ENDPOINT = "https://api.replit.com/v1/repls/{repl_id}/files/{file_path}"

def get_ai_suggestion():
    """Simulate AI generating a suggestion."""
    return random.choice(AI_SUGGESTIONS)

def sync_with_replit(code, repl_id, file_path, api_key):
    """Sync code with a Replit repl."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "content": code
    }
    response = requests.post(
        REPLIT_API_ENDPOINT.format(repl_id=repl_id, file_path=file_path),
        headers=headers,
        data=json.dumps(data)
    )
    return response.status_code == 200

def main():
    st.title("AI-Enhanced Code Collaboration Tool with Replit Integration")

    # Initialize session state
    if 'code' not in st.session_state:
        st.session_state.code = ""
    if 'ai_suggestion' not in st.session_state:
        st.session_state.ai_suggestion = ""

    # Replit configuration
    st.sidebar.subheader("Replit Configuration")
    repl_id = st.sidebar.text_input("Repl ID")
    file_path = st.sidebar.text_input("File Path")
    api_key = st.sidebar.text_input("Replit API Key", type="password")

    # Code Editor
    st.subheader("Code Editor")
    new_code = st.text_area("Write your code here:", value=st.session_state.code, height=300, key="code_editor")

    # Check if code has changed
    if new_code != st.session_state.code:
        st.session_state.code = new_code
        st.session_state.ai_suggestion = get_ai_suggestion()

    # AI Assistant
    st.subheader("AI Assistant")
    if st.session_state.ai_suggestion:
        st.info(f"AI Assistant: {st.session_state.ai_suggestion}")
    
    # Button to manually trigger AI suggestion
    if st.button("Get AI Suggestion"):
        st.session_state.ai_suggestion = get_ai_suggestion()
        st.experimental_rerun()

    # Sync with Replit
    if st.button("Sync with Replit"):
        if repl_id and file_path and api_key:
            if sync_with_replit(st.session_state.code, repl_id, file_path, api_key):
                st.success("Successfully synced with Replit!")
            else:
                st.error("Failed to sync with Replit. Please check your configuration.")
        else:
            st.warning("Please fill in all Replit configuration fields.")

if __name__ == "__main__":
    main()