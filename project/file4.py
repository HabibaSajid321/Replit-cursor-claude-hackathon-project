import streamlit as st
import requests
import json
import random
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT  # Import Claude integration

# Simulated AI suggestions (we'll replace this with Cursor and Claude later)
AI_SUGGESTIONS = [
    "Consider using a list comprehension here.",
    "This loop could be optimized using enumerate().",
    "Don't forget to add error handling for this function.",
    "You might want to consider breaking this into smaller functions.",
    "Remember to add docstrings to your functions.",
]

# Replit API endpoint (replace with actual endpoint when available)
REPLIT_API_ENDPOINT = "https://api.replit.com/v1/repls/{repl_id}/files/{file_path}"

# Cursor API endpoint (placeholder - replace with actual endpoint)
CURSOR_API_ENDPOINT = "https://api.cursor.sh/v1/analyze"

def get_ai_suggestion(code):
    """Get AI suggestion using Cursor's API."""
    # This is a placeholder. In reality, you'd call Cursor's API here.
    return random.choice(AI_SUGGESTIONS)

def get_claude_review(code, anthropic_api_key):
    """Get code review from Claude."""
    # Set up the Claude client with the API key
    client = Anthropic(api_key=anthropic_api_key)
    prompt = f"{HUMAN_PROMPT} Please review the following code and provide suggestions for improvement:\n\n{code}\n{AI_PROMPT}"

    # Call Claude's API for a code review
    response = client.completions.create(
        model="claude-2",
        prompt=prompt,
        max_tokens_to_sample=150
    )
    return response["completion"].strip()

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
    st.title("AI-Enhanced Code Collaboration Tool with Replit and Cursor Integration")

    # Initialize session state
    if 'code' not in st.session_state:
        st.session_state.code = ""
    if 'ai_suggestion' not in st.session_state:
        st.session_state.ai_suggestion = ""
    if 'claude_review' not in st.session_state:
        st.session_state.claude_review = ""

    # Replit configuration
    st.sidebar.subheader("Replit Configuration")
    repl_id = st.sidebar.text_input("Repl ID")
    file_path = st.sidebar.text_input("File Path")
    api_key = st.sidebar.text_input("Replit API Key", type="password")

    # Anthropic API Key for Claude
    anthropic_api_key = st.sidebar.text_input("Anthropic API Key", type="password")

    # Code Editor
    st.subheader("Code Editor")
    new_code = st.text_area("Write your code here:", value=st.session_state.code, height=300, key="code_editor")

    # Check if code has changed
    if new_code != st.session_state.code:
        st.session_state.code = new_code
        st.session_state.ai_suggestion = get_ai_suggestion(new_code)
        if anthropic_api_key:
            st.session_state.claude_review = get_claude_review(new_code, anthropic_api_key)

    # AI Assistant (Cursor)
    st.subheader("Cursor AI Assistant")
    if st.session_state.ai_suggestion:
        st.info(f"Cursor: {st.session_state.ai_suggestion}")

    # Claude Review
    st.subheader("Claude Code Review")
    if st.session_state.claude_review:
        st.info(f"Claude: {st.session_state.claude_review}")

    # Button to manually trigger AI suggestion and Claude review
    if st.button("Get AI Feedback"):
        st.session_state.ai_suggestion = get_ai_suggestion(st.session_state.code)
        if anthropic_api_key:
            st.session_state.claude_review = get_claude_review(st.session_state.code, anthropic_api_key)
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
