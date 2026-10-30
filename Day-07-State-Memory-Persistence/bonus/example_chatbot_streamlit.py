"""Day 7 (flavor 4): the SQLite-backed chatbot graph, reused by example_chatbot_streamlit_ui.py."""

import os
import sqlite3

import ollama
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from typing import TypedDict

# keep the database next to this file, whichever folder you run from
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day7_chatbot_memory.db")


class ChatState(TypedDict, total=False):
    user_message: str
    chat_history: list[dict]
    reply: str


def chatbot(state):
    history = state.get("chat_history", []) + [{"role": "user", "content": state["user_message"]}]
    response = ollama.chat(model="gpt-oss:120b-cloud", messages=history)
    reply = response["message"]["content"]
    history = history + [{"role": "assistant", "content": reply}]
    return {"chat_history": history, "reply": reply}


graph_builder = StateGraph(ChatState)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Same db file as example_chatbot_sqlite.py -> both programs share saved history.
connection = sqlite3.connect(DB_PATH, check_same_thread=False)
checkpointer = SqliteSaver(connection)
graph = graph_builder.compile(checkpointer=checkpointer)
