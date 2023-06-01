import gradio as gr
import os
from tutorials_generator.template_generator import TemplateGenerator
from tutorials_generator.content_generator import ContentGenerator

def generate_content(topic, identity, target_audience, model, tutorial_output_file, wiki_output_file):
    # Generate and save the template
    progress_text = "Generating template..."
    template_generator = TemplateGenerator(topic, identity, target_audience)
    tutorial_template_file = "tutorial_template.json"
    wiki_template_file = "wiki_template.json"
    template_generator.save_tutorial_template_to_file(tutorial_template_file)
    template_generator.save_wiki_template_to_file(wiki_template_file)

    # Generate cell content using the ContentGenerator
    progress_text = "Generating cell content..."
    cg = ContentGenerator(model=model)
    cg.create_notebook(tutorial_template_file, tutorial_output_file)
    cg.create_wiki(wiki_template_file, wiki_output_file)

    tutorial_url = f"/output/{tutorial_output_file}"
    wiki_url = f"/output/{wiki_output_file}"
    
    # Return a dictionary with the output URLs and progress text
    output_urls = {
        "Tutorial URL": tutorial_url,
        "Wiki URL": wiki_url
    }
    return output_urls, "Content generated successfully"


# Define the input and output types for the Gradio interface
inputs = [
    gr.inputs.Textbox(label="Topic"),
    gr.inputs.Textbox(label="Identity", default="Professor of Computer Science"),
    gr.inputs.Textbox(label="Target Audience", default="first year computer science students"),
    gr.inputs.Dropdown(["gpt-3.5-turbo", "gpt-4"], label="Model"),
    gr.inputs.Textbox(label="Tutorial Output File", default="output.ipynb"),
    gr.inputs.Textbox(label="Wiki Output File", default="output.md")
]
output = [
    gr.outputs.Textbox(label="Progress"),
    gr.outputs.Textbox(label="Download Tutorial URL"),
    gr.outputs.Textbox(label="Download Wiki URL")
]

# Create the Gradio interface
iface = gr.Interface(
    generate_content,
    inputs=inputs,
    outputs=output,
    title="Content Generator",
    description="Generate content from a template",
    theme="default"
)

# Define the output directory for the download links
output_dir = "output"

# Launch the Gradio interface
iface.launch(inbrowser=True)

# After the interface is closed, delete any output files that were generated
if os.path.exists(output_dir):
    for file in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, file))
    os.rmdir(output_dir)
