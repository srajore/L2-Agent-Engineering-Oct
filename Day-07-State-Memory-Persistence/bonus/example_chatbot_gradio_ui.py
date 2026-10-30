r"""Day 7 (flavor 4 UI): Gradio chat window for the SQLite-backed graph.

Run this file with::

    uv run python Day-07-State-Memory-Persistence\bonus\example_chatbot_gradio_ui.py

from the repository root (needs `ollama signin`).
"""

import uuid

import gradio as gr

from example_chatbot_streamlit import graph


WELCOME_MESSAGE = {
    "role": "assistant",
    "content": "Hi! Send a message to start this thread's conversation.",
}

CSS = """
.gradio-container { max-width: 900px !important; margin: 0 auto !important; }
.chat-header {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    border-radius: 14px;
    padding: 1.1rem 1.4rem;
    margin-bottom: 1.2rem;
    color: white;
}
.chat-header h1 { font-size: 1.3rem; margin: 0; }
.chat-header p { margin: 0.2rem 0 0; opacity: 0.9; font-size: 0.85rem; }
"""


def settings_for(thread_id: str) -> dict:
    """Build the LangGraph configuration for one conversation thread."""
    return {"configurable": {"thread_id": thread_id.strip() or "student-1"}}


def saved_history(thread_id: str) -> list[dict]:
    """Load a thread's persisted messages for display."""
    state = graph.get_state(settings_for(thread_id))
    history = state.values.get("chat_history", [])
    return list(history) or [WELCOME_MESSAGE]


def load_thread(thread_id: str):
    """Show the saved conversation when the selected thread changes."""
    return saved_history(thread_id), gr.Textbox(value="", interactive=True), False


def start_new_chat():
    """Create a fresh thread and reset the chat controls."""
    thread_id = uuid.uuid4().hex[:8]
    return thread_id, [WELCOME_MESSAGE], gr.Textbox(value="", interactive=True), False


def send_message(message: str, thread_id: str, stopped: bool):
    """Send one message to the graph and refresh the persisted history."""
    if stopped:
        return saved_history(thread_id), gr.Textbox(value="", interactive=False), True

    message = message.strip()
    if not message:
        return saved_history(thread_id), gr.Textbox(value="", interactive=True), False

    if message.lower() in ("bye", "quit"):
        history = saved_history(thread_id)
        if history == [WELCOME_MESSAGE]:
            history = []
        history.append({"role": "assistant", "content": "Goodbye!"})
        return history, gr.Textbox(value="", interactive=False), True

    graph.invoke({"user_message": message}, config=settings_for(thread_id))
    return saved_history(thread_id), gr.Textbox(value="", interactive=True), False


with gr.Blocks(title="Day 7 Chatbot") as demo:
    stopped = gr.State(False)

    gr.HTML(
        """
        <div class="chat-header">
            <h1>Day 7 Chatbot</h1>
            <p>SQLite-backed memory - type "bye" or "quit" to end the conversation</p>
        </div>
        """
    )

    with gr.Row():
        thread_id = gr.Textbox(
            value="student-1",
            label="Thread ID",
            info="Different Thread IDs never share history.",
            scale=4,
        )
        new_chat_button = gr.Button("New chat", variant="secondary", scale=1)

    chatbot = gr.Chatbot(
        value=[WELCOME_MESSAGE],
        height=500,
        show_label=False,
    )

    with gr.Row():
        message = gr.Textbox(
            placeholder="Type a message ('bye' or 'quit' to stop)",
            show_label=False,
            lines=1,
            scale=5,
        )
        send_button = gr.Button("Send", variant="primary", scale=1)

    submit_inputs = [message, thread_id, stopped]
    submit_outputs = [chatbot, message, stopped]

    message.submit(send_message, submit_inputs, submit_outputs)
    send_button.click(send_message, submit_inputs, submit_outputs)
    thread_id.change(load_thread, thread_id, submit_outputs)
    new_chat_button.click(
        start_new_chat,
        outputs=[thread_id, chatbot, message, stopped],
    )
    demo.load(load_thread, thread_id, submit_outputs)


if __name__ == "__main__":
    demo.queue(default_concurrency_limit=1).launch(css=CSS)
