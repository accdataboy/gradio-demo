"""Gradio demo by Chris Pitchford. Reference: https://gradio.app/guides/quickstart """
from pathlib import Path
import gradio as gr

DEFAULT_IMAGE = Path(__file__).parent / "assets" / "default-shutterstock.jpg"

def welcome_baby(
    name: str,
    gender: str | None,
    birthdate: str,
    photo: str | None,
) -> tuple[str, str | None]:
    """Create a welcome message and return the selected baby photo."""
    baby_name = name.strip() or "the little darling"
    baby_gender = gender or "not selected"
    baby_birthdate = birthdate or "not provided"

    message = (
        f"Welcome, {baby_name}!\n\n"
        f"Gender: {baby_gender}\n"
        f"Birthday: {baby_birthdate}"
    )
    return message, photo

demo = gr.Interface(
    fn=welcome_baby,
    inputs=[
        gr.Textbox(label="New baby's name", placeholder="Enter a name"),
        gr.Radio(["Boy", "Girl"], label="New baby's gender", value=None),
        gr.DateTime(
            label="Date of Birth",
            include_time=False,
            type="string",
        ),
        gr.Image(
            value=str(DEFAULT_IMAGE),
            label="Baby photo",
            type="filepath",
            sources=["upload"],
        ),
    ],
    outputs=[
        gr.Textbox(label="Welcome message"),
        gr.Image(label="Photo preview", type="filepath"),
    ],
    title="Welcome, New Baby!",
    description="Provide some details for the new baby to create a welcome message. If you want, upload a photo, too.",
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch()
