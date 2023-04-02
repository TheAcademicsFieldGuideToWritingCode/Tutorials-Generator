import argparse
from curriculum_module_generator.template_generator import TemplateGenerator
from curriculum_module_generator.content_generator import ContentGenerator

def cli():
    parser = argparse.ArgumentParser(description="Generate content from a template")
    parser.add_argument("--topic", required=True, help="The topic for the content")
    parser.add_argument("--identity", default="Professor of Computer Science", help="The identity of the content creator")
    parser.add_argument("--target_audience", default="first year computer science students", help="The target audience for the content")
    parser.add_argument('--tutorial_output_file', type=str, default="output.ipynb", help='Path to the tutorial output file. Defaults to output.ipynb.')
    parser.add_argument('--wiki_output_file', type=str, default="output.md", help='Path to the wiki output file. Defaults to output.md.')
    parser.add_argument('--model', type=str, default="gpt-3.5-turbo", help='The OpenAI GPT model to use for generating cell content. Defaults to gpt-3.5-turbo.')

    args = parser.parse_args()

    main(args.topic, args.identity, args.target_audience, args.model, args.tutorial_output_file, args.wiki_output_file)

def main(topic, identity, target_audience, model, tutorial_output_file, wiki_output_file):
    # Generate and save the template
    template_generator = TemplateGenerator(topic, identity, target_audience)
    # tutorial_template = template_generator.generate_tutorial_template()
    # wiki_template = template_generator.generate_wiki_template()
    tutorial_template_file = "tutorial_template.json"
    wiki_template_file = "wiki_template.json"
    template_generator.save_tutorial_template_to_file(tutorial_template_file)
    template_generator.save_wiki_template_to_file(wiki_template_file)

    # Generate cell content using the ContentGenerator
    cg = ContentGenerator(model=model)
    cg.create_notebook(tutorial_template_file, tutorial_output_file)
    cg.create_wiki(wiki_template_file, wiki_output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate content from a template")
    parser.add_argument("--topic", required=True, help="The topic for the content")
    parser.add_argument("--identity", default="Professor of Computer Science", help="The identity of the content creator")
    parser.add_argument("--target_audience", default="first year computer science students", help="The target audience for the content")
    parser.add_argument('--tutorial_output_file', type=str, default="output.ipynb", help='Path to the tutorial output file. Defaults to output.ipynb.')
    parser.add_argument('--wiki_output_file', type=str, default="output.md", help='Path to the wiki output file. Defaults to output.md.')
    parser.add_argument('--model', type=str, default="gpt-3.5-turbo", help='The OpenAI GPT model to use for generating cell content. Defaults to gpt-3.5-turbo.')

    args = parser.parse_args()

    main(args.topic, args.identity, args.target_audience, args.model, args.tutorial_output_file, args.wiki_output_file)
