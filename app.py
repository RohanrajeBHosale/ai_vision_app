import gradio as gr
from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import torch

# 1. Load the model and processor
print("Loading AI Model... Please wait.")
model_name = "dandelin/vilt-b32-finetuned-vqa"
processor = ViltProcessor.from_pretrained(model_name)
model = ViltForQuestionAnswering.from_pretrained(model_name)

def answer_question(image, text):
    try:
        if image is None or text == "":
            return "Please upload an image and ask a question."

        # 2. Prepare the inputs for the model
        encoding = processor(image, text, return_tensors="pt")

        # 3. Forward pass (The "Thinking" step)
        with torch.no_grad():
            outputs = model(**encoding)

        # 4. Find the highest probability answer
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        answer = model.config.id2label[idx]

        return answer.capitalize()

    except Exception as e:
        return f"Error: {str(e)}"

# 5. Build the Gradio Interface
# Note: flagging_mode="never" is the correct syntax for Gradio 5.x/6.x
demo = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Ask a question about this image", placeholder="e.g. What color is the car?")
    ],
    outputs=gr.Textbox(label="AI's Answer"),
    title="👁️ Visual AI Assistant",
    description="Upload an image and ask a question. This app uses a Vision-and-Language Transformer (ViLT) to 'see' and 'chat'.",
    flagging_mode="never"
)

# 6. Launch the app
if __name__ == "__main__":
    demo.launch()