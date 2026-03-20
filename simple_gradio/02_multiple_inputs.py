import gradio as gr

def build_profile(name: str, age: int, language: str):
    """Build a profile card from user inputs"""
    profile = f"""Profile Card
    - **Name:** {name}
    - **Age:** {age}
    - **Language:** {language}
    - **Status:** {"student" if age < 25 else "Professional"}
    """
    fun_fact = f"{name} has been alive for approximately {age * 365} days"

    return profile, fun_fact

demo = gr.Interface(
    fn=build_profile,
    inputs=[
        gr.Textbox(label="Name", placeholder="Enter your name"),
        gr.Slider(minimum=10, maximum=100, value=20, step=1, label="Age"),
        gr.Dropdown(
            choices=["Python", "JavaScript", "Java", "C++", "Go"],
            value="Python", # default
            label="Favorite Language"
        ),
    ],
    outputs=[
        gr.Markdown(label="Profile Card"),
        gr.Textbox(label="Fun fact")
    ],
    title="Profile Builder",
    description="Enter your details and get your profile card",
    flagging_mode="never"
)

if __name__ == "__main__":
    demo.launch()