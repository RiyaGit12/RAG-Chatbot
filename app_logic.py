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

#     prompt = f"""
# You are a STRICT MySQL query generator.

# Table: {table_name}

# Allowed columns ONLY:
# {columns_list}

# User question:
# {user_question}

# STRICT RULES:
# - ONLY use columns from the list
# - DO NOT guess column names
# - DO NOT create new columns
# - ONLY SELECT query
# - ALWAYS add LIMIT 5
# - If unsure, return: SELECT * FROM {table_name} LIMIT 5
# - NO explanation

# SQL:
# """

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": prompt}]
#     )

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
#             return {"answer": "No relevant data found.", "sql": ""}

#         table_meta = next(t for t in metadata if t["table_name"] == table_name)

#         sql = generate_sql(user_input, table_name, table_meta)

#         if not sql.lower().startswith("select"):
#             return {"answer": "Unsafe query blocked.", "sql": sql}

#         try:
#             cursor.execute(sql)
#             result = cursor.fetchall()
#         except Exception:
#             fallback_sql = f"SELECT * FROM {table_name} LIMIT 5"
#             cursor.execute(fallback_sql)
#             result = cursor.fetchall()
#             sql = fallback_sql

#         if not result:
#             return {"answer": "No data available.", "sql": sql}

#         answer = summarize_answer(user_input, result)
#         return {"answer": answer, "sql": sql}

#     except Exception as e:
#         return {"answer": f"System Error: {str(e)}", "sql": ""}
import os
import json
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
            return {"answer": "No relevant data found."}

        table_meta = next(t for t in metadata if t["table_name"] == table_name)

        sql = generate_sql(user_input, table_name, table_meta)

        if not sql.lower().startswith("select"):
            return {"answer": "Unsafe query blocked."}

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception:
            fallback_sql = f"SELECT * FROM {table_name} LIMIT 5"
            cursor.execute(fallback_sql)
            result = cursor.fetchall()

        if not result:
            return {"answer": "No data available."}

        answer = summarize_answer(user_input, result)
        return {"answer": answer}

    except Exception as e:
        return {"answer": f"System Error: {str(e)}"}