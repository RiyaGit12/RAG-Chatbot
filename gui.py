# import os
# import tkinter as tk
# from tkinter import scrolledtext
# from dotenv import load_dotenv
# from google import genai

# # Load env
# load_dotenv()

# # Gemini client
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# # -------- function --------
# def send_message():
#     user_text = entry.get().strip()

#     if user_text == "":
#         return

#     chat_box.config(state=tk.NORMAL)
#     chat_box.insert(tk.END, "You: " + user_text + "\n")
#     entry.delete(0, tk.END)

#     try:
#         response = client.models.generate_content(
#             model="models/gemini-flash-latest",
#             contents=user_text
#         )
#         chat_box.insert(tk.END, "AI: " + response.text + "\n\n")
#     except Exception as e:
#         chat_box.insert(tk.END, "Error: " + str(e) + "\n")

#     chat_box.config(state=tk.DISABLED)
#     chat_box.see(tk.END)

# # -------- GUI --------
# root = tk.Tk()
# root.title("AI Chatbot")
# root.geometry("500x520")

# chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
# chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# bottom_frame = tk.Frame(root)
# bottom_frame.pack(fill=tk.X, padx=10, pady=5)

# entry = tk.Entry(bottom_frame)
# entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

# send_button = tk.Button(
#     bottom_frame,
#     text="Send",
#     width=10,
#     command=send_message
# )
# send_button.pack(side=tk.RIGHT)

# root.mainloop()
import os
import json
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
from google import genai
import mysql.connector

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- DB ----------------
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor()

# ---------------- GEMINI ----------------
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ---------------- METADATA ----------------
with open("metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

# ---------------- LOGIC FUNCTIONS ----------------
def rank_tables(user_query):
    user_query = user_query.lower()
    scores = []

    for table in metadata:
        text = (
            table["table_name"] +
            table["description"]
        ).lower()

        score = sum(1 for w in user_query.split() if w in text)
        scores.append((table["table_name"], score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0]

def generate_sql(question, table):
    prompt = f"""
Generate MySQL query only.

Question:
{question}

Table:
{table}
"""
    return client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    ).text.strip()

def summarize(question, result):
    prompt = f"""
Question:
{question}

Data:
{result}

Explain simply.
"""
    return client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    ).text.strip()

# ---------------- GUI FUNCTION ----------------
def send_message():
    user_text = entry.get().strip()
    if not user_text:
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_text}\n")
    entry.delete(0, tk.END)

    try:
        table = rank_tables(user_text)
        sql = generate_sql(user_text, table)
        cursor.execute(sql)
        result = cursor.fetchall()
        answer = summarize(user_text, result)

        chat_box.insert(tk.END, f"AI: {answer}\n\n")
    except Exception as e:
        chat_box.insert(tk.END, f"Error: {e}\n\n")

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

# ---------------- GUI LAYOUT ----------------
root = tk.Tk()
root.title("Govt Data AI Chatbot")
root.geometry("520x550")

chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

bottom = tk.Frame(root)
bottom.pack(fill=tk.X, padx=10, pady=5)

entry = tk.Entry(bottom)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

send_btn = tk.Button(bottom, text="Send", width=10, command=send_message)
send_btn.pack(side=tk.RIGHT)

root.mainloop()
