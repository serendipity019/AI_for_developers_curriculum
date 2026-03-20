import gradio as gr

def add_item(item: str, current_list: list):
    if not item.strip():
        return current_list, format_list(current_list), "Type something first"
    
    current_list = current_list + [item.strip()]
    return current_list, format_list(current_list), f"Added: {item}"

def clear_list():
    return [], "List Cleared", "Your list is empty" 

def format_list(items: list) -> str:
    if not items:
        return "Your list is empty"
    
    lines = [f"{i + 1}. {item}" for i, item in enumerate(items)]
    return "### Shopping List\n" + "\n".join(lines) + f"\n\n**Total: {len(items)} items**"

with gr.Blocks(title="Shopping List") as demo:
    gr.Markdown("# Interactive Shopping List")
    gr.Markdown("Learn how **Buttons**, **State** and **Events** work in Gradio")

    # gr.State stores data between interactions (invisible to user)
    shopping_list = gr.State([])

    with gr.Row():  # Make a row box 
        item_input = gr.Textbox(
            label="Add Item",
            placeholder="Type an item and click Add...",
            scale=3 # mean 3/4 of box length
        )
        add_btn = gr.Button("Add", variant="primary", scale=1) # mean 1/4 of box length
    
    clear_btn = gr.Button("Clear All", variant="secondary")

    list_display = gr.Markdown("*Your list is empty*")
    status = gr.Textbox(label="Status", interactive=False)

    add_btn.click(
        fn= add_item,
        inputs=[item_input, shopping_list],
        outputs=[shopping_list, list_display, status]
    )

    clear_btn.click(
        fn=clear_list,
        inputs=[],
        outputs=[shopping_list, list_display, status]
    )


if __name__ == "__main__":
    demo.launch()