import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Bihar Government Data Chatbot",
    page_icon="🌳",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #f5f7fb, #eef2ff);
}

.block-container {
    padding-top: 2rem;
}

.stChatMessage {
    border-radius: 12px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🌿 About Project")

    st.markdown("### 📊 Features")
    st.markdown("- 🌳 Forest Cover")
    st.markdown("- 🏞️ Zoo Tourism")
    st.markdown("- 🌱 Nursery Reports")
    st.markdown("- 📜 Land Schemes")

    st.markdown("### ⚙️ Tech Stack")
    st.markdown("- Python")
    st.markdown("- MySQL")
    st.markdown("- Groq API (LLM)")
    st.markdown("- Streamlit")

# ---------------- HEADER ----------------
st.title("🤖 Bihar Government Data Chatbot")
st.caption("Ask questions about Bihar forest, tourism & land data")

# ---------------- CHAT DISPLAY ----------------
<<<<<<< HEAD
for role, msg in st.session_state.chat:
    cls = "user" if role == "You" else "bot"
    st.markdown(
        f"<div class='chat-box'><span class='{cls}'>{role}:</span><br>{msg}</div>",
        unsafe_allow_html=True
    )
=======
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Type your question here...")

if user_input:
    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):
            try:
                from app_logic import ask_question
                response = ask_question(user_input)

                if not response or response.strip() == "":
                    response = "No response received. Please try again."

            except Exception as e:
                response = f"⚠️ Backend Error: {str(e)}"

        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

