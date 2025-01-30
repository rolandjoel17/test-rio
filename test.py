import streamlit as st
from streamlit_chat import message

# Set page configuration
st.set_page_config(
    page_title="Custom Chat Interface",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar for customization
st.sidebar.header("Customize Chat")
background_color = st.sidebar.color_picker("Pick a background color", "#ffffff")
text_color = st.sidebar.color_picker("Pick a text color", "#000000")

# Add logo
uploaded_logo = st.sidebar.file_uploader("Upload a logo (optional)", type=["png", "jpg", "jpeg"])

# Display the logo if uploaded
if uploaded_logo:
    st.image(uploaded_logo, use_column_width=True)

# Style settings
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {background_color};
            color: {text_color};
        }}
        .message { background-color: #f1f1f1; padding: 10px; border-radius: 5px; margin: 10px 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Custom Chat Interface")

# Input area
user_input = st.text_input("You:", key="user_input")
if st.button("Send") and user_input.strip():
    st.session_state.messages.append({"user": "You", "content": user_input})
    st.session_state.messages.append({"user": "Bot", "content": f"You said: {user_input}"})
    st.experimental_rerun()

# Display messages
for msg in st.session_state.messages:
    if msg["user"] == "You":
        message(msg["content"], is_user=True)
    else:
        message(msg["content"])
