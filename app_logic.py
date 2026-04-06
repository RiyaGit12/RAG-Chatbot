
# import os
# import json
# import time
# from dotenv import load_dotenv
# import mysql.connector
# import google.generativeai as genai

# # ---------------- LOAD ENV ----------------
# load_dotenv()

# # ---------------- GEMINI CONFIG ----------------
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # ⚡ FAST & STABLE MODEL
# model = genai.GenerativeModel("gemini-1.5-flash")

# # ---------------- DB CONNECTION ----------------
# db = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME"),
#     connection_timeout=5
# )
# cursor = db.cursor()

# # ---------------- LOAD METADATA ----------------
# with open("metadata.json", "r", encoding="utf-8") as f:
#     metadata = json.load(f)

# # ---------------- TABLE RANKING ----------------
# def rank_tables(user_query):
#     user_query = user_query.lower()
#     scores = []

#     for table in metadata:
#         searchable_text = (
#             table["table_name"]
#             + table.get("description", "")
#             + table.get("department", "")
#             + table.get("sector", "")
#         ).lower()

#         score = sum(word in searchable_text for word in user_query.split())
#         scores.append((table["table_name"], score))

#     scores.sort(key=lambda x: x[1], reverse=True)
#     return scores[0]

# # ---------------- SQL GENERATION ----------------
# def generate_sql(user_question, table_name, table_metadata):
#     columns = ", ".join(table_metadata.get("columns", []))

#     prompt = f"""
# You are an expert MySQL assistant.

# Table name: {table_name}
# Available columns: {columns}

# User question:
# {user_question}

# Rules:
# - Generate ONLY SELECT query
# - Use ONLY column names from the list
# - Do NOT invent column names
# - Add LIMIT 5
# - No explanation

# SQL:
# """
#     start = time.time()
#     response = model.generate_content(prompt)

#     # ⏱ Timeout safety
#     if time.time() - start > 8:
#         raise Exception("SQL generation timeout")

#     return response.text.replace("```sql", "").replace("```", "").strip()

# # ---------------- SUMMARIZATION (ENGLISH ONLY) ----------------
# def summarize_answer(user_question, db_result):
#     prompt = f"""
# User question:
# {user_question}

# Database result:
# {db_result}

# Explain the result in clear, simple, professional English.
# No Hindi.
# """

#     start = time.time()
#     response = model.generate_content(prompt)

#     # ⏱ Timeout safety
#     if time.time() - start > 8:
#         raise Exception("Answer summarization timeout")

#     return str(response.text.strip())

# # ---------------- MAIN FUNCTION (STREAMLIT USES THIS) ----------------
# def ask_question(user_input):
#     try:
#         table_name, score = rank_tables(user_input)

#         if score == 0:
#             return "Sorry, no relevant government data found for this query."

#         table_meta = next(t for t in metadata if t["table_name"] == table_name)

#         sql = generate_sql(user_input, table_name, table_meta)

#         if not sql.lower().startswith("select"):
#             return "Unsafe query blocked."

#         cursor.execute(sql)
#         result = cursor.fetchall()

#         if not result:
#             return "No data available for this query."

#         answer = summarize_answer(user_input, result)

#         # 🔒 Final safety
#         if not answer or answer.strip() == "":
#             return "The system could not generate a response. Please try again."

#         return answer

#     except Exception as e:
#         return f"System/API error: {str(e)}"

# import os
# import json
# import time
# from dotenv import load_dotenv
# import mysql.connector
# import google.generativeai as genai

# # ---------------- LOAD ENV ----------------
# load_dotenv()

# # ---------------- GEMINI CONFIG ----------------
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # ✅ FIXED MODEL
# model = genai.GenerativeModel("gemini-pro")

# # ---------------- DB CONNECTION ----------------
# db = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME"),
#     connection_timeout=5
# )
# cursor = db.cursor()

# # ---------------- LOAD METADATA ----------------
# with open("metadata.json", "r", encoding="utf-8") as f:
#     metadata = json.load(f)

# # ---------------- TABLE RANKING ----------------
# def rank_tables(user_query):
#     user_query = user_query.lower()
#     scores = []

#     for table in metadata:
#         searchable_text = (
#             table["table_name"]
#             + table.get("description", "")
#             + table.get("department", "")
#             + table.get("sector", "")
#         ).lower()

#         score = sum(word in searchable_text for word in user_query.split())
#         scores.append((table["table_name"], score))

#     scores.sort(key=lambda x: x[1], reverse=True)
#     return scores[0]

# # ---------------- SQL GENERATION ----------------
# def generate_sql(user_question, table_name, table_metadata):
#     columns = ", ".join(table_metadata.get("columns", []))

#     prompt = f"""
# You are an expert MySQL assistant.

# Table name: {table_name}
# Available columns: {columns}

# User question:
# {user_question}

# Rules:
# - Generate ONLY SELECT query
# - Use ONLY column names
# - Add LIMIT 5
# - No explanation

# SQL:
# """
#     response = model.generate_content(prompt)
#     return response.text.replace("```sql", "").replace("```", "").strip()

# # ---------------- SUMMARIZATION ----------------
# def summarize_answer(user_question, db_result):
#     prompt = f"""
# User question:
# {user_question}

# Database result:
# {db_result}

# Explain in simple English.
# """
#     response = model.generate_content(prompt)
#     return response.text.strip()

# # ---------------- MAIN FUNCTION ----------------
# def ask_question(user_input):
#     try:
#         table_name, score = rank_tables(user_input)

#         if score == 0:
#             return "No relevant data found."

#         table_meta = next(t for t in metadata if t["table_name"] == table_name)

#         sql = generate_sql(user_input, table_name, table_meta)

#         if not sql.lower().startswith("select"):
#             return "Unsafe query blocked."

#         cursor.execute(sql)
#         result = cursor.fetchall()

#         if not result:
#             return "No data available."

#         answer = summarize_answer(user_input, result)
#         return answer

#     except Exception as e:
#         return f"System Error: {str(e)}"
# import os
# import json
# import time
# from dotenv import load_dotenv
# import mysql.connector
# from groq import Groq

# # ---------------- LOAD ENV ----------------
# load_dotenv()

# # ---------------- GROQ CONFIG ----------------
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# # ---------------- DB CONNECTION ----------------
# db = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME"),
#     connection_timeout=5
# )
# cursor = db.cursor()

# # ---------------- LOAD METADATA ----------------
# with open("metadata.json", "r", encoding="utf-8") as f:
#     metadata = json.load(f)

# # ---------------- TABLE RANKING ----------------
# def rank_tables(user_query):
#     user_query = user_query.lower()
#     scores = []

#     for table in metadata:
#         searchable_text = (
#             table["table_name"]
#             + table.get("description", "")
#             + table.get("department", "")
#             + table.get("sector", "")
#         ).lower()

#         score = sum(word in searchable_text for word in user_query.split())
#         scores.append((table["table_name"], score))

#     scores.sort(key=lambda x: x[1], reverse=True)
#     return scores[0]

# # ---------------- SQL GENERATION ----------------
# def generate_sql(user_question, table_name, table_metadata):
#     columns = ", ".join(table_metadata.get("columns", []))

#     prompt = f"""
# You are an expert MySQL assistant.

# Table name: {table_name}
# Available columns: {columns}

# User question:
# {user_question}

# Rules:
# - Generate ONLY SELECT query
# - Use ONLY given columns
# - Add LIMIT 5
# - No explanation

# SQL:
# """

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response.choices[0].message.content.strip()


# # ---------------- SUMMARIZATION ----------------
# def summarize_answer(user_question, db_result):
#     prompt = f"""
# User question:
# {user_question}

# Database result:
# {db_result}

# Explain in simple English.
# """

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response.choices[0].message.content.strip()


# # ---------------- MAIN FUNCTION ----------------
# def ask_question(user_input):
#     try:
#         table_name, score = rank_tables(user_input)

#         if score == 0:
#             return "No relevant data found."

#         table_meta = next(t for t in metadata if t["table_name"] == table_name)

#         sql = generate_sql(user_input, table_name, table_meta)

#         if not sql.lower().startswith("select"):
#             return "Unsafe query blocked."

#         cursor.execute(sql)
#         result = cursor.fetchall()

#         if not result:
#             return "No data available."

#         answer = summarize_answer(user_input, result)
#         return answer

#     except Exception as e:
#         return f"System Error: {str(e)}"
# import os
# import json
# import time
# from dotenv import load_dotenv
# import mysql.connector
# from groq import Groq

# # ---------------- LOAD ENV ----------------
# load_dotenv()

# # ---------------- GROQ CONFIG ----------------
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# # ---------------- DB CONNECTION ----------------
# db = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME"),
#     connection_timeout=5
# )
# cursor = db.cursor()

# # ---------------- LOAD METADATA ----------------
# with open("metadata.json", "r", encoding="utf-8") as f:
#     metadata = json.load(f)

# # ---------------- TABLE RANKING ----------------
# def rank_tables(user_query):
#     user_query = user_query.lower()
#     scores = []

#     for table in metadata:
#         searchable_text = (
#             table["table_name"]
#             + table.get("description", "")
#             + table.get("department", "")
#             + table.get("sector", "")
#         ).lower()

#         score = sum(word in searchable_text for word in user_query.split())
#         scores.append((table["table_name"], score))

#     scores.sort(key=lambda x: x[1], reverse=True)
#     return scores[0]

# # ---------------- SQL GENERATION ----------------
# def generate_sql(user_question, table_name, table_metadata):
#     columns_list = table_metadata.get("columns", [])
#     columns = ", ".join(columns_list)

#     prompt = f"""
# You are a strict MySQL query generator.

# Table name: {table_name}
# Allowed columns: {columns}

# User question:
# {user_question}

# STRICT RULES:
# - Use ONLY columns from the given list
# - DO NOT guess column names
# - DO NOT create new column names
# - ONLY SELECT query
# - Add LIMIT 5
# - No explanation

# Return ONLY SQL query.
# """

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     # ✅ CLEAN SQL OUTPUT
#     sql = response.choices[0].message.content
#     sql = sql.replace("```sql", "").replace("```", "").strip()

#     return sql


# # ---------------- SUMMARIZATION ----------------
# def summarize_answer(user_question, db_result):
#     prompt = f"""
# User question:
# {user_question}

# Database result:
# {db_result}

# Explain in simple English.
# """

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response.choices[0].message.content.strip()


# # ---------------- MAIN FUNCTION ----------------
# def ask_question(user_input):
#     try:
#         table_name, score = rank_tables(user_input)

#         if score == 0:
#             return "No relevant data found."

#         table_meta = next(t for t in metadata if t["table_name"] == table_name)

#         sql = generate_sql(user_input, table_name, table_meta)

#         # 🔒 SAFETY CHECK
#         if not sql.lower().startswith("select"):
#             return "Unsafe query blocked."

#         # 🔒 COLUMN VALIDATION (NEW FIX)
#         allowed_columns = set(table_meta.get("columns", []))
#         words = sql.replace(",", " ").replace("(", " ").replace(")", " ").split()

#         for word in words:
#             if word.isidentifier() and word not in allowed_columns and word.lower() not in ["select", "from", "where", "limit", "count", "*"]:
#                 return "Query used invalid column. Try rephrasing."

#         cursor.execute(sql)
#         result = cursor.fetchall()

#         if not result:
#             return "No data available."

#         answer = summarize_answer(user_input, result)
#         return answer

#     except Exception as e:
#         return f"System Error: {str(e)}"
import os
import json
import time
from dotenv import load_dotenv
import mysql.connector
from groq import Groq

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- GROQ CONFIG ----------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- DB CONNECTION ----------------
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    connection_timeout=5
)
cursor = db.cursor()

# ---------------- LOAD METADATA ----------------
with open("metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

# ---------------- TABLE RANKING ----------------
def rank_tables(user_query):
    user_query = user_query.lower()
    scores = []

    for table in metadata:
        searchable_text = (
            table["table_name"]
            + table.get("description", "")
            + table.get("department", "")
            + table.get("sector", "")
        ).lower()

        score = sum(word in searchable_text for word in user_query.split())
        scores.append((table["table_name"], score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0]

# ---------------- SQL GENERATION ----------------
def generate_sql(user_question, table_name, table_metadata):
    columns_list = table_metadata.get("columns", [])

    prompt = f"""
You are a STRICT MySQL query generator.

Table: {table_name}

Allowed columns ONLY:
{columns_list}

User question:
{user_question}

STRICT RULES:
- ONLY use columns from the list
- DO NOT guess column names
- DO NOT create new columns
- ONLY SELECT query
- ALWAYS add LIMIT 5
- If unsure, return: SELECT * FROM {table_name} LIMIT 5
- NO explanation

SQL:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    sql = response.choices[0].message.content
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql

# ---------------- SUMMARIZATION ----------------
def summarize_answer(user_question, db_result):
    prompt = f"""
User question:
{user_question}

Database result:
{db_result}

Explain in simple English.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# ---------------- MAIN FUNCTION ----------------
def ask_question(user_input):
    try:
        table_name, score = rank_tables(user_input)

        if score == 0:
            return "No relevant data found."

        table_meta = next(t for t in metadata if t["table_name"] == table_name)

        sql = generate_sql(user_input, table_name, table_meta)

        # 🔒 ONLY SELECT ALLOWED
        if not sql.lower().startswith("select"):
            return "Unsafe query blocked."

        # 🔒 SAFE EXECUTION WITH FALLBACK
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception:
            # ✅ fallback if query fails
            fallback_sql = f"SELECT * FROM {table_name} LIMIT 5"
            cursor.execute(fallback_sql)
            result = cursor.fetchall()

        if not result:
            return "No data available."

        answer = summarize_answer(user_input, result)
        return answer

    except Exception as e:
        return f"System Error: {str(e)}"