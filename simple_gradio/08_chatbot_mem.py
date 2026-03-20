import os

from pathlib import Path
from dotenv import  load_dotenv
import gradio as gr

load_dotenv(Path.cwd().parent / "API_Verifications/.env")
    

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "").strip().strip('"').strip("'")
)

OPENAI_MODEL = "gpt-4o-mini"
if client:
    print(f"OpenAI client ready - using model {OPENAI_MODEL}")

SYSTEM_PROMPT = """You are a friendly and helpfull assistant.
You remember everything the user has said in this conversation.
Be concise but warm. Use emoji occasionally."""

def chat_with_memory(message: str, history: list):
    messages = [
        {"role": "system", "content":SYSTEM_PROMPT},
        *history,
        {"role": "user", "content": message},
    ]

    try:
        stream = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            stream=True,
            max_tokens= 500
        )

        partial = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                partial += delta
                yield partial
    except Exception as e:
        yield f"Error: {e}"

demo = gr.ChatInterface(
    fn=chat_with_memory,
    title="Chat with OpenAI and memory",
    description="This chatbot remembers everything...",
    examples=[
        "What is Python in one sentence?",
        "My name is Alice. I am 30 years old and I am software developer",
        "Explain APIs like i'm 10 years old."
    ]
)        

if __name__ == "__main__":
    demo.launch()
