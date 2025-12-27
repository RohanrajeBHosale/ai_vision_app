# 👁️ Visual AI Assistant (VQA)

**"A picture is worth a thousand words—now you can ask the AI for the right ones."**

This is a **Visual Question Answering (VQA)** application that allows users to upload an image and ask natural language questions about its content. It uses a **Multimodal Transformer** (ViLT) to process both visual pixels and text queries simultaneously to provide real-time, accurate answers.

---

## 🚀 Features

* **Multimodal Reasoning:** Seamlessly combines Computer Vision and Natural Language Processing.
* **Local Inference:** Runs entirely on your machine. No API keys required, ensuring privacy and zero costs.
* **Zero-Shot Analysis:** Identifies colors, counts objects, and recognizes actions in images it has never seen before.
* **Modern UI:** Built with **Gradio 6.x** for a responsive, browser-based experience.

---

## 🧠 What is Multimodal AI?

Multimodal AI represents a system that can understand information from different sources (modalities), such as text and images, at the same time. 

This app uses the **ViLT (Vision-and-Language Transformer)** model. Unlike traditional models that analyze an image and then "attach" text to it later, ViLT is trained to look at both the image and the question at once, mimicking the way human brains process visual and verbal information together.

---

## 🛠️ Tech Stack

* **Model:** `dandelin/vilt-b32-finetuned-vqa` (via Hugging Face)
* **Frontend:** [Gradio](https://gradio.app/)
* **Deep Learning:** [PyTorch](https://pytorch.org/) & [Transformers](https://huggingface.co/docs/transformers/index)
* **Image Processing:** [Pillow (PIL)](https://python-pillow.org/)

---

## ⚙️ Setup & Installation

### 1. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```


##2. Install Dependencies
```
pip install gradio transformers torch Pillow
```

## 📂 Project Structure
app.py: The core application code, including model loading, prediction logic, and the UI layout.
README.md: Project documentation and instructions.


##🖥️ Usage
Run the Application:
```
python3 app.py
```
Note: The first launch will download approximately 470MB of model weights from Hugging Face. This will be cached for future use.)
Access the Interface:
Open the local URL provided in the terminal (usually http://127.0.0.1:7860).
Sample Queries to Try:
Counting: "How many people are in the picture?"
Color: "What color is the car on the left?"
Activity: "Is the person sitting or standing?"
Detail: "What is written on the sign?"

##💡 Technical Note
This implementation is optimized for Gradio 6.x. If you encounter errors with "flagging" in older tutorials, note that allow_flagging has been replaced by flagging_mode="never" in the interface definition.

##Built with ❤️ using Hugging Face Transformers and Gradio.
