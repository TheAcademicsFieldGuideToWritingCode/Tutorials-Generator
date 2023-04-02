import argparse
import nbformat as nbf
from tqdm import tqdm
from content_generator import ContentGenerator

def main(config_file, output_file='output.ipynb', model='gpt-3.5-turbo'):
    """
    Create a new Jupyter Notebook from a configuration file and save it to a file.

    Args:
        config_file (str): The path to a JSON configuration file.
        output_file (str): The path to the output file. Defaults to 'output.ipynb'.
        model (str): The OpenAI GPT model to use for generating cell content. Defaults to 'gpt-3.5-turbo'.
    """
    cg = ContentGenerator(model=model)
    nb = cg.create_notebook(config_file)
    nbf.write(nb, output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a Jupyter Notebook from a JSON configuration file.')
    parser.add_argument('--config_file', type=str, help='Path to the JSON configuration file.')
    parser.add_argument('--output_file', type=str, help='Path to the output file. Defaults to output.ipynb.')
    parser.add_argument('--model', type=str, help='The OpenAI GPT model to use for generating cell content. Defaults to gpt-3.5-turbo.')
    args = parser.parse_args()

    output_file = args.output_file or 'output.ipynb'
    model = args.model or 'gpt-3.5-turbo'
    main(args.config_file, output_file=output_file, model=model)
