"""Gradio demo by Chris Pitchford. Reference: https://gradio.app/guides/quickstart """
import gradio as gr

def welcome_baby(name: str) -> tuple[str]:
    """Create a welcome message."""
    baby_name = name.strip() or "little darling"
    message = (
        f"Welcome, {baby_name}!"
    )
    return message

demo = gr.Interface(
    fn=welcome_baby,
    inputs=[
        gr.Textbox(label="New baby's name", placeholder="Enter a name")
    ],
    outputs=[
        gr.Textbox(label="Welcome message")
    ],
    title="Welcome, New Baby!",
    description="Provide the new baby's name to create a welcome message.",
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch()
