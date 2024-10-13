import streamlit as st
import os
import random
import time

# Simulated AI suggestions (enhanced)
AI_SUGGESTIONS = {
    "python": [
        "Consider using a list comprehension here for more concise code.",
        "This loop could be optimized using enumerate() for better readability.",
        "Don't forget to add error handling to make your function more robust.",
        "You might want to consider breaking this into smaller functions for better maintainability.",
        "Remember to add docstrings to your functions to improve documentation.",
        "Consider using a context manager (with statement) for file operations.",
        "You could use f-strings for more readable string formatting.",
        "Think about adding type hints to improve code clarity and catch potential type-related bugs.",
    ],
    "javascript": [
        "Consider using arrow functions for more concise syntax.",
        "You could use destructuring assignment to simplify variable declarations.",
        "Don't forget to use 'const' for variables that won't be reassigned.",
        "Consider using template literals for multi-line strings or string interpolation.",
        "Remember to add JSDoc comments for better documentation.",
        "You might want to use async/await for handling asynchronous operations more cleanly.",
    ]
}

def get_ai_suggestion(language):
    """Generate an AI suggestion based on the programming language."""
    return random.choice(AI_SUGGESTIONS.get(language, AI_SUGGESTIONS["python"]))

def save_code(filename, code):
    """Save code to a local file."""
    with open(filename, 'w') as f:
        f.write(code)

def load_code_from_file(file):
    """Load code from an uploaded file."""
    if file is not None:
        return file.read().decode("utf-8")
    return ""

def main():
    st.title("AI-Enhanced Code Collaboration Tool")

    # Initialize session state
    if 'code' not in st.session_state:
        st.session_state.code = ""
    if 'ai_suggestion' not in st.session_state:
        st.session_state.ai_suggestion = ""
    if 'language' not in st.session_state:
        st.session_state.language = "python"
    if 'filename' not in st.session_state:
        st.session_state.filename = "code.py"

    # Sidebar for file operations and language selection
    st.sidebar.subheader("File Operations")
    uploaded_file = st.sidebar.file_uploader("Load a file", type=["py", "js", "txt"])
    if uploaded_file:
        st.session_state.code = load_code_from_file(uploaded_file)
        st.session_state.filename = uploaded_file.name
    
    # Display the filename in the text input
    st.session_state.filename = st.sidebar.text_input("Filename", st.session_state.filename)
    
    if st.sidebar.button("Save"):
        save_code(st.session_state.filename, st.session_state.code)
        st.sidebar.success(f"Saved to {st.session_state.filename}")

    st.sidebar.subheader("Language")
    st.session_state.language = st.sidebar.selectbox("Select Language", ["python", "javascript"])

    # Code Editor
    st.subheader("Code Editor")
    new_code = st.text_area("Write your code here:", value=st.session_state.code, height=300, key="code_editor")

    # Check if code has changed
    if new_code != st.session_state.code:
        st.session_state.code = new_code
        st.session_state.ai_suggestion = get_ai_suggestion(st.session_state.language)

    # AI Assistant
    st.subheader("AI Assistant")
    if st.session_state.ai_suggestion:
        st.info(f"AI Assistant: {st.session_state.ai_suggestion}")
    
    # Button to manually trigger AI suggestion
    if st.button("Get AI Suggestion"):
        st.session_state.ai_suggestion = get_ai_suggestion(st.session_state.language)
        st.experimental_rerun()

    # Simulated real-time updates
    placeholder = st.empty()
    for i in range(10):
        time.sleep(2)
        placeholder.info(f"Simulated update {i+1}: Last edit was {i*2} seconds ago")

if __name__ == "__main__":
    main()
