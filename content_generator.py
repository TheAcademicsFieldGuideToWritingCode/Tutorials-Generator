import os
import openai
import nbformat as nbf
import markdown
import json
import uuid
from tqdm import tqdm
from block import Block
from cell_type import CellType
from block_factory import BlockFactory


class ContentGenerator:
    def __init__(self, model="gpt-3.5-turbo", system_block=None, max_tokens=1024, n=1, stop=None, temperature=0.7):
        self.model = model
        self.system_block = system_block
        self.max_tokens = max_tokens
        self.n = n
        self.stop = stop
        self.temperature = temperature
        self._set_api_key()

    def _set_api_key(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("Environment variable OPENAI_API_KEY not set")

    def generate_block_content(self, block):
        print(block.generate_prompt())
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.system_block.generate_prompt(),
                },
                {"role": "user", "content": block.generate_prompt()},
            ],
            max_tokens=self.max_tokens,
            n=self.n,
            stop=self.stop,
            temperature=self.temperature,
        )
        print(response["choices"])
        block.set_content(response["choices"][0]["message"]["content"])

    def generate_all_block_content(self, blocks):
        with tqdm(total=len(blocks), desc="Generating block content") as pbar:
            for block in blocks:
                self.generate_block_content(block)
                pbar.update(1)

    def create_notebook(self, config_file):
        nb = nbf.v4.new_notebook()
        blocks = self._create_content(config_file)
        self._generate_notebook_blocks(blocks, nb)
        return nb

    def _generate_notebook_blocks(self, blocks, nb):
        print(blocks)
        for block in blocks:
            if block.cell_type == CellType.CODE:
                new_cell = nbf.v4.new_code_cell(block.content)
                new_cell['id'] = str(uuid.uuid4())  # Generate and set cell id
                nb.cells.append(new_cell)
            elif block.cell_type == CellType.MARKDOWN:
                nb.cells.append(nbf.v4.new_markdown_cell(block.content))
        print(nb)
        return nb
    
    def create_markdown_file(self, blocks, file_path):
        with open(file_path, "w") as f:
            for block in blocks:
                f.write(markdown.markdown(block.content))

    def _create_content(self, config_file):
        blocks = self.parse_config_file(config_file)
        self.update_context(config_file, blocks)

        if blocks[0].type == 'SeedBlock':
            self.system_block = blocks[0]
            blocks.pop(0)
        else:
            self.system_block = None

        self.generate_all_block_content(blocks)
        return blocks

    @staticmethod
    def update_context(config_file, blocks):
        with open(config_file) as f:
            config = json.load(f)
            for block, block_config in zip(blocks, config['blocks']):
                if 'context' in block_config and block_config['context'] is not None:
                    block.set_context(blocks[block_config['context']])
    @staticmethod
    def parse_config_file(config_file):
        with open(config_file) as f:
            config = json.load(f)
            blocks = []
            for block_config in config['blocks']:
                block = BlockFactory.create_block(block_config)
                blocks.append(block)
            return blocks
