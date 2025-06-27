import gradio as gr
import ollama

# Function to interact with the DeepscalerR Chatbot
def chatbot(message):
    response = ollama.chat(
        model='deepscaler',
        messages=[{'role': 'user', 'content': message}]
    )
    return response['message']['content']

# Build a Gradio interface
chatbot_ui = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(label="📝 Enter Your Message Here"),
    outputs=gr.Textbox(label="📘 Bot Response "),
    title="🤖 AI-Powered Chatbot",
    description="Chat with an AI Chatbot powered by DeepScaleR and Ollama.",
    examples=[
        ["Hi, How are you?"],
        ["What is AI?"],
        ["What is Ollama?"]
    ],
    # live=True,  # Enables dynamic updates
    theme="soft"  # Optional: aesthetic theme
)

# Launch the app
if __name__ == "__main__":
    chatbot_ui.launch(show_error=True)

