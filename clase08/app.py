import gradio
demo = gradio.Blocks()
with demo:
    gradio.Markdown("Registro")
    gradio.Textbox(label="nombre:")
    gradio.Button("Enviar")

demo.launch()    
        