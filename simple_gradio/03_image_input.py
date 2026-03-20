import gradio as gr 
from PIL import ImageFilter, Image

def process_image(image, effect):
    """Apply a visual effect to an uploaded image"""
    if image is None:
        return None, "Please upload an image first"
    
    img = Image.fromarray(image)
    if effect == "Blur":
        result = img.filter(ImageFilter.GaussianBlur(radius=5))
    elif effect == "Sharpen":
        result = img.filter(ImageFilter.SHARPEN)
    elif effect == "Edges":
        result = img.filter(ImageFilter.FIND_EDGES)
    elif effect == "Grayscale":
        result = img.convert("L")
    else:
        result = img

    info = f"**Original:** {img.size[0]}X{img.size[1]}px | **Effect:** {effect}"

    return result, info

demo = gr.Interface(
    fn= process_image,
    inputs=[
        gr.Image(label="Upload an Image"),
        gr.Radio(
            choices=["Blur", "Sharpen", "Edges", "Grayscale"],
            value="Grayscale",
            label="Effect"
        ),
    ],
    outputs=[
        gr.Image(label="Result"),
        gr.Markdown(label="Info")
    ],
    title="Image Effects",
    description="Upload an image and apply a filter",
    flagging_mode='never'
)


 
if __name__ == "__main__":
    demo.launch()