import gradio as gr

def greet(name):
    print(f"Hello {name} welcome back!")
    return f"Hello, {name}. Welcome to AI for Developers"

demo = gr.Interface(
    fn= greet,
    inputs= gr.Textbox(label= "Your name", placeholder= "Type your name..."),
    outputs= gr.Textbox(label= "Greeting"),
    title= "Welcome AI for Developers",
    description= "Type your name and get a greeting",
    flagging_mode= "never" # This is to make saves. We can have manual to save with button or auto to save in every case

)

if __name__ == "__main__":
    demo.launch()
    # demo.launch(share=True) # This instead of above allow us to share the link public.   

