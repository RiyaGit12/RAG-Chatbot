import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Bihar Government Data Chatbot",
    page_icon="🌳",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# 🔥 FIX: unique key
if "input_text_riya" not in st.session_state:
    st.session_state.input_text_riya = ""

# ---------------- CSS ----------------
st.markdown("""
<style>
.chat-box {
    background-color: #ffffff;
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.user { color: #0d6efd; font-weight: 600; }
.bot { color: #198754; font-weight: 500; }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🌿 About Project")
    st.markdown("""
**Bihar Government Data Chatbot**

• Forest Cover  
• Zoo Tourism  
• Nursery Reports  
• Land Schemes  

**Tech Stack**
- Python  
- MySQL  
- Gemini AI  
- Streamlit
""")

# ---------------- MAIN ----------------
st.title("🤖 Bihar Government Data Chatbot")
st.caption("Ask questions related to forest, environment & land data of Bihar")

# ---------------- FUNCTION ----------------
def submit():
    question = st.session_state.input_text_riya

    if not question.strip():
        st.warning("Please type a question first.")
        return

    st.session_state.chat.append(("You", question))

    with st.spinner("Fetching government data..."):
        try:
            from app_logic import ask_question
            answer = ask_question(question)

            if not answer or answer.strip() == "":
                answer = "No response received. Please try again."

        except Exception as e:
            answer = f"⚠️ Backend Error: {str(e)}"

    st.session_state.chat.append(("Bot", answer))

# ---------------- INPUT ----------------
st.text_input("Type your question 👇", key="input_text_riya")

# ---------------- BUTTON ----------------
# 🔥 FIX: unique key added
st.button("Ask Question", on_click=submit, key="ask_btn_riya")

# ---------------- CHAT DISPLAY ----------------
for role, msg in st.session_state.chat:
    cls = "user" if role == "You" else "bot"
    st.markdown(
        f"<div class='chat-box'><span class='{cls}'>{role}:</span><br>{msg}</div>",
        unsafe_allow_html=True
    )
