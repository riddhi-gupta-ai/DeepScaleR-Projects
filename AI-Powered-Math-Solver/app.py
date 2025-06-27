import gradio as gr
import ollama

# Function to process and solve math problems
def solve_math_problem(problem):
    response = ollama.chat(
        model='deepscaler',
        messages=[{'role': 'user', 'content': problem}]
    )
    return response['message']['content']

# Build a Gradio interface
interface = gr.Interface(
    fn=solve_math_problem,
    inputs=gr.Text(label="📝 Enter Your Math Problem"),
    outputs=gr.Textbox(label="📘 Step-by-Step Solution"),
    title="📐 AI-Powered Math Solver",
    description="Ask any math question (algebra, calculus, equations, etc.) and DeepScalerR will solve it step-by-step.",
    examples=[
        ["Solve: 2x + 3 = 11"],
        ["What is the derivative of sin(x)?"],
        ["Integrate x^2 dx"],
        ["Factor: x^2 + 5x + 6"]
    ],
    theme="soft"  # Optional: aesthetic theme
)

# Launch the app
if __name__ == "__main__":
    interface.launch(show_error=True)
