import gradio as gr
from index_plate_calculator import calculate_turns

indexer = gr.Interface(
    fn=calculate_turns, 
    inputs=gr.Number(label="Enter the number of teeth of the gear"), 
    outputs=gr.Textbox(label="Result"),
    title="Index Plate Calculator",
    description="This tool will guide you in selecting the right indexing plate for your Brown and Sharpe indexing head."
)

if __name__ == "__main__":
    indexer.launch()