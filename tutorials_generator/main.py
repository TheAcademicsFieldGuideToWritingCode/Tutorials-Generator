import click
import json
import os
from tutorials_generator.template_generator import TemplateGenerator
from tutorials_generator.content_generator import ContentGenerator


def create_module(topic, identity = 'professor of computer science', target_audience='first year computer science students', tutorial_output_file='output.ipynb', wiki_output_file='output.md', model='gpt-3.5-turbo'):

    # Generate and save the template
    template_generator = TemplateGenerator(topic, identity, target_audience)
    tutorial_template_file = 'tutorial_template.json'
    wiki_template_file = 'wiki_template.json'
    template_generator.save_tutorial_template_to_file(tutorial_template_file)
    template_generator.save_wiki_template_to_file(wiki_template_file)

    # Generate cell content using the ContentGenerator
    cg = ContentGenerator(model=model)
    cg.create_notebook(tutorial_template_file, tutorial_output_file)
    cg.create_wiki(wiki_template_file, wiki_output_file)


@click.group()
def cli():
    pass


@click.command()
@click.option('--topic', help='The topic for the content')
@click.option('--identity', default='Professor of Computer Science', help='The identity of the content creator')
@click.option('--target_audience', default='first year computer science students', help='The target audience for the content')
@click.option('--tutorial_output_file', type=click.Path(), default='output.ipynb', help='Path to the tutorial output file. Defaults to output.ipynb.')
@click.option('--wiki_output_file', type=click.Path(), default='output.md', help='Path to the wiki output file. Defaults to output.md.')
@click.option('--model', type=str, default='gpt-3.5-turbo', help='The OpenAI GPT model to use for generating cell content. Defaults to gpt-3.5-turbo.')
@click.option('--interactive', '-i', is_flag=True, help='Interactive mode')
def module(topic, identity, target_audience, tutorial_output_file, wiki_output_file, model, interactive):
    if interactive:
        topic = click.prompt('Enter the topic for the content')
        identity = click.prompt(
            'Enter the identity of the content creator', default='Professor of Computer Science')
        target_audience = click.prompt(
            'Enter the target audience for the content', default='first year computer science students')
        tutorial_output_file = click.prompt(
            'Enter the path to the tutorial output file', default='output.ipynb')
        wiki_output_file = click.prompt(
            'Enter the path to the wiki output file', default='output.md')
        model = click.prompt(
            'Enter the OpenAI GPT model to use for generating cell content', default='gpt-3.5-turbo')

    # Generate and save the template
    template_generator = TemplateGenerator(topic, identity, target_audience)
    tutorial_template_file = 'tutorial_template.json'
    wiki_template_file = 'wiki_template.json'
    template_generator.save_tutorial_template_to_file(tutorial_template_file)
    template_generator.save_wiki_template_to_file(wiki_template_file)

    # Generate cell content using the ContentGenerator
    cg = ContentGenerator(model=model)
    cg.create_notebook(tutorial_template_file, tutorial_output_file)
    cg.create_wiki(wiki_template_file, wiki_output_file)


@click.option('--identity', default='Professor of Computer Science', help='The identity of the content creator')
@click.option('--target_audience', default='first year computer science students', help='The target audience for the content')
@click.option('--model', type=str, default='gpt-3.5-turbo', help='The OpenAI GPT model to use for generating cell content. Defaults to gpt-3.5-turbo.')
@click.option('--curriculum_file', help="file containing the curriculum")
@click.option('--interactive', '-i', is_flag=True, help='Interactive mode')
@click.command()
def curriculum(identity, target_audience, model, curriculum_file, interactive):
    if interactive:
        curriculum_file = click.prompt('Enter the path to the curriculum file')
        model = click.prompt(
            'Enter the OpenAI GPT model to use for generating cell content', default='gpt-3.5-turbo')

    if not curriculum_file:
        raise click.UsageError("A curriculum file must be provided.")

    with open(curriculum_file) as f:
        curriculum_data = json.load(f)

    if 'topics' not in curriculum_data:
        raise click.UsageError(
            "The curriculum file must contain a 'topics' key with a list of topics.")

    os.makedirs("Curriculum/Wiki", exist_ok=True)
    os.makedirs("Curriculum/Interactive_Tutorials", exist_ok=True)

    for topic_index, topic in enumerate(curriculum_data['topics']):
        topic_name = topic['name']
        os.makedirs(f"Curriculum/Wiki/{topic_name}", exist_ok=True)
        os.makedirs(
            f"Curriculum/Interactive_Tutorials/{topic_name}", exist_ok=True)

        for subtopic_index, subtopic in enumerate(topic['subtopics']):
            tutorial_output_file = f"Curriculum/Interactive_Tutorials/{topic_name}/subtopic_{subtopic_index}.ipynb"
            wiki_output_file = f"Curriculum/Wiki/{topic_name}/subtopic_{subtopic_index}.md"
            create_module(subtopic, identity, target_audience,
                   tutorial_output_file, wiki_output_file, model)

    # loops through module creation based on the contents of the curriculum file
    # the curriculum file will contain a json object that contains a list of topics
    # we will assume that eacch topic will become a module and use the same target audience, mrtywerydel, and identity


cli.add_command(module)
cli.add_command(curriculum)

if __name__ == '__main__':
    cli()
