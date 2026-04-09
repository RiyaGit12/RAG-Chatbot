# # # import streamlit as st

# # # # ---------------- PAGE CONFIG ----------------
# # # st.set_page_config(
# # #     page_title="Bihar Government Data Chatbot",
# # #     page_icon="🌳",
# # #     layout="wide"
# # # )

# # # # ---------------- SESSION STATE ----------------
# # # if "messages" not in st.session_state:
# # #     st.session_state.messages = []

# # # # ---------------- CUSTOM CSS ----------------
# # # st.markdown("""
# # # <style>
# # # .main {
# # #     background: linear-gradient(to right, #f5f7fb, #eef2ff);
# # # }

# # # .block-container {
# # #     padding-top: 2rem;
# # # }

# # # .stChatMessage {
# # #     border-radius: 12px;
# # #     padding: 10px;
# # # }

# # # </style>
# # # """, unsafe_allow_html=True)

# # # # ---------------- SIDEBAR ----------------
# # # with st.sidebar:
# # #     st.title("🌿 About Project")

# # #     st.markdown("### 📊 Features")
# # #     st.markdown("- 🌳 Forest Cover")
# # #     st.markdown("- 🏞️ Zoo Tourism")
# # #     st.markdown("- 🌱 Nursery Reports")
# # #     st.markdown("- 📜 Land Schemes")

# # #     st.markdown("### ⚙️ Tech Stack")
# # #     st.markdown("- Python")
# # #     st.markdown("- MySQL")
# # #     st.markdown("- Groq API (LLM)")
# # #     st.markdown("- Streamlit")

# # # # ---------------- HEADER ----------------
# # # st.title("🤖 Bihar Government Data Chatbot")
# # # st.caption("Ask questions about Bihar forest, tourism & land data")

# # # # ---------------- CHAT DISPLAY ---------------
# # # for role, msg in st.session_state.chat:
# # #     cls = "user" if role == "You" else "bot"
# # #     st.markdown(
# # #         f"<div class='chat-box'><span class='{cls}'>{role}:</span><br>{msg}</div>",
# # #         unsafe_allow_html=True
# # #     )

# # # for msg in st.session_state.messages:
# # #     with st.chat_message(msg["role"]):
# # #         st.markdown(msg["content"])

# # # # ---------------- CHAT INPUT ----------------
# # # user_input = st.chat_input("Type your question here...")

# # # if user_input:
# # #     # User message
# # #     st.session_state.messages.append({
# # #         "role": "user",
# # #         "content": user_input
# # #     })

# # #     with st.chat_message("user"):
# # #         st.markdown(user_input)

# # #     # Bot response
# # #     with st.chat_message("assistant"):
# # #         with st.spinner("Thinking... 🤖"):
# # #             try:
# # #                 from app_logic import ask_question
# # #                 response = ask_question(user_input)

# # #                 if not response or response.strip() == "":
# # #                     response = "No response received. Please try again."

# # #             except Exception as e:
# # #                 response = f"⚠️ Backend Error: {str(e)}"

# # #         st.markdown(response)

# # #     st.session_state.messages.append({
# # #         "role": "assistant",
# # #         "content": response
# # #     })

# # import streamlit as st

# # # ---------------- PAGE CONFIG ----------------
# # st.set_page_config(
# #     page_title="Bihar Government Data Chatbot",
# #     page_icon="🌳",
# #     layout="wide"
# # )

# # # ---------------- SESSION STATE ----------------
# # if "messages" not in st.session_state:
# #     st.session_state.messages = []

# # # ---------------- CUSTOM CSS ----------------
# # st.markdown("""
# # <style>
# # .main {
# #     background: linear-gradient(to right, #f5f7fb, #eef2ff);
# # }

# # .block-container {
# #     padding-top: 2rem;
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # # ---------------- SIDEBAR ----------------
# # with st.sidebar:
# #     st.title("🌿 About Project")

# #     st.markdown("### 📊 Features")
# #     st.markdown("- 🌳 Forest Cover")
# #     st.markdown("- 🏞️ Zoo Tourism")
# #     st.markdown("- 🌱 Nursery Reports")
# #     st.markdown("- 📜 Land Schemes")

# #     st.markdown("### ⚙️ Tech Stack")
# #     st.markdown("- Python")
# #     st.markdown("- MySQL")
# #     st.markdown("- Groq API (LLaMA 3)")
# #     st.markdown("- Streamlit")

# # # ---------------- HEADER ----------------
# # st.title("🤖 Bihar Government Data Chatbot")
# # st.caption("Ask questions about Bihar forest, tourism & land data")

# # # ---------------- CHAT DISPLAY ----------------
# # for msg in st.session_state.messages:
# #     with st.chat_message(msg["role"]):
# #         st.markdown(msg["content"])

# # # ---------------- CHAT INPUT ----------------
# # user_input = st.chat_input("Type your question here...")

# # if user_input:
# #     # ---------------- USER MESSAGE ----------------
# #     st.session_state.messages.append({
# #         "role": "user",
# #         "content": user_input
# #     })

# #     with st.chat_message("user"):
# #         st.markdown(user_input)

# #     # ---------------- BOT RESPONSE ----------------
# #     with st.chat_message("assistant"):
# #         with st.spinner("Thinking... 🤖"):
# #             try:
# #                 from app_logic import ask_question
# #                 response = ask_question(user_input)

# #                 # ✅ Safety guard
# #                 if isinstance(response, dict):
# #                     answer = response.get("answer", "No response received.")
# #                     sql = response.get("sql", "")
# #                 else:
# #                     answer = str(response)
# #                     sql = ""

# #             except Exception as e:
# #                 answer = f"⚠️ Backend Error: {str(e)}"
# #                 sql = ""

# #         # Show Answer
# #         st.markdown(answer)

# #         # Show SQL (for interview 🔥)
# #         if sql:
# #             with st.expander("🔍 View Generated SQL"):
# #                 st.code(sql, language="sql")

# #     # ---------------- SAVE BOT RESPONSE ----------------
# #     st.session_state.messages.append({
# #         "role": "assistant",
# #         "content": answer
# #     })
# import streamlit as st

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Bihar Government Data Chatbot",
#     page_icon="🌳",
#     layout="wide"
# )

# # ---------------- SESSION STATE ----------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>
# .main {
#     background: linear-gradient(to right, #f5f7fb, #eef2ff);
# }

# .block-container {
#     padding-top: 2rem;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- SIDEBAR ----------------
# with st.sidebar:
#     st.title("🌿 About Project")

#     st.markdown("### 📊 Features")
#     st.markdown("- 🌳 Forest Cover")
#     st.markdown("- 🏞️ Zoo Tourism")
#     st.markdown("- 🌱 Nursery Reports")
#     st.markdown("- 📜 Land Schemes")

#     st.markdown("### ⚙️ Tech Stack")
#     st.markdown("- Python")
#     st.markdown("- MySQL")
#     st.markdown("- Groq API (LLaMA 3)")
#     st.markdown("- Streamlit")

# # ---------------- HEADER ----------------
# st.title("🤖 Bihar Government Data Chatbot")
# st.caption("Ask questions about Bihar forest, tourism & land data")

# # ---------------- CHAT DISPLAY ----------------
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # ---------------- CHAT INPUT ----------------
# user_input = st.chat_input("Type your question here...")

# if user_input:
#     # ---------------- USER MESSAGE ----------------
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user_input
#     })

#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # ---------------- BOT RESPONSE ----------------
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking... 🤖"):
#             try:
#                 from app_logic import ask_question
#                 response = ask_question(user_input)

#                 if isinstance(response, dict):
#                     answer = response.get("answer", "No response received.")
#                 else:
#                     answer = str(response)

#             except Exception as e:
#                 answer = f"⚠️ Backend Error: {str(e)}"

#         st.markdown(answer)

#     # ---------------- SAVE BOT RESPONSE ----------------
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": answer
#     })
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

/* ---- Background ---- */
.main {
    background: linear-gradient(135deg, #f0f4ff, #e8f5e9);
}

.block-container {
    padding-top: 2rem;
}

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e8f5e9, #dce8ff);
    border-right: 1px solid #c8d8e8;
}

[data-testid="stSidebar"] h1 {
    color: #2e7d32;
    font-size: 1.3rem;
}

/* ---- Buttons ---- */
.stButton > button {
    background-color: #e8f0fe;
    color: #1a73e8;
    border: 1px solid #1a73e8;
    border-radius: 20px;
    padding: 0.4rem 1.2rem;
    font-size: 0.85rem;
    transition: all 0.2s ease;
    width: 100%;
}

.stButton > button:hover {
    background-color: #1a73e8;
    color: white;
    border-color: #1a73e8;
}

/* ---- Chat messages ---- */
.stChatMessage {
    border-radius: 16px;
    padding: 0.5rem;
    margin-bottom: 0.4rem;
}

/* ---- Chat input ---- */
.stChatInput textarea {
    border-radius: 20px !important;
    border: 1.5px solid #1a73e8 !important;
    padding: 0.6rem 1rem !important;
}

/* ---- Title ---- */
h1 {
    color: #1b5e20;
    font-weight: 700;
}

/* ---- Caption ---- */
.stCaption {
    color: #555;
    font-size: 0.9rem;
}

/* ---- Expander ---- */
.streamlit-expanderHeader {
    border-radius: 12px;
    background-color: #f0f4ff;
}

/* ---- Scrollbar ---- */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-thumb {
    background: #1a73e8;
    border-radius: 10px;
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

    st.markdown("---")

    st.markdown("### ⚙️ Tech Stack")
    st.markdown("- Python")
    st.markdown("- MySQL")
    st.markdown("- Groq API (LLaMA 3)")
    st.markdown("- Streamlit")

# ---------------- HEADER ----------------
st.title("🤖 Bihar Government Data Chatbot")
st.caption("Ask questions about Bihar forest, tourism & land data")

st.markdown("---")

# ---------------- CHAT DISPLAY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Type your question here...")

if user_input:
    # ---------------- USER MESSAGE ----------------
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------------- BOT RESPONSE ----------------
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):
            try:
                from app_logic import ask_question
                response = ask_question(user_input)

                if isinstance(response, dict):
                    answer = response.get("answer", "No response received.")
                else:
                    answer = str(response)

            except Exception as e:
                answer = f"⚠️ Backend Error: {str(e)}"

        st.markdown(answer)

    # ---------------- SAVE BOT RESPONSE ----------------
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })