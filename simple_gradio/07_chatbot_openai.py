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

def chat(message: str, history: list):
    try:
        stream = client.chat.completions.create(
            model= OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Be concise."},
                {"role": "user", "content":message}
            ],
            stream= True,
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
    fn= chat,
    title="OpenAI Chatbot",
    description=(
        "Chat with GPT-4o-mini - responses stream in real-time"
        "No memory - each message is independent!"
    ),
    examples = [
        "What is Python in one sentence?",
        "Write a haiku about programming",
        "Explain APIs like i'm 10 years old."
    ]
)

if __name__ == "__main__":
    demo.launch()
