import os
import openai
import nbformat as nbf
import markdown
import json
import uuid
from tqdm import tqdm
from cell import Cell
from cell_type import CellType
from cell_factory import CellFactory 


class ContentGenerator:
    def __init__(self, model="gpt-3.5-turbo", system_cell=None, max_tokens=1024, n=1, stop=None, temperature=0.7):
        self.model = model
        self.system_cell = system_cell
        self.max_tokens = max_tokens
        self.n = n
        self.stop = stop
        self.temperature = temperature
        self._set_api_key()

    def _set_api_key(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("Environment variable OPENAI_API_KEY not set")

    def generate_cell_content(self, cell):
        print(cell.generate_prompt())
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.system_cell.generate_prompt(),
                },
                {"role": "user", "content": cell.generate_prompt()},
            ],
            max_tokens=self.max_tokens,
            n=self.n,
            stop=self.stop,
            temperature=self.temperature,
        )
        print(response["choices"])
        cell.set_content(response["choices"][0]["message"]["content"])

    def generate_all_cell_content(self, cells):
        with tqdm(total=len(cells), desc="Generating cell content") as pbar:
            for cell in cells:
                self.generate_cell_content(cell)
                pbar.update(1)

    def create_notebook(self, config_file):
        nb = nbf.v4.new_notebook()
        cells = self._create_content(config_file)
        self._generate_notebook_cells(cells, nb)
        return nb

    def _generate_notebook_cells(self, blocks, nb):
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
    
    def create_markdown_file(self, cells, file_path):
        with open(file_path, "w") as f:
            for cell in cells:
                f.write(markdown.markdown(cell.content))

    def _create_content(self, config_file):
        cells = self.parse_config_file(config_file)
        self.update_context(config_file, cells)

        if cells[0].type == 'SeedCell':
            self.system_cell = cells[0]
            cells.pop(0)
        else:
            self.system_cell = None

        self.generate_all_cell_content(cells)
        return cells

    @staticmethod
    def update_context(config_file, cells):
        with open(config_file) as f:
            config = json.load(f)
            for cell, cell_config in zip(cells, config['cells']):
                if 'context' in cell_config and cell_config['context'] is not None:
                    cell.set_context(cells[cell_config['context']])
    @staticmethod
    def parse_config_file(config_file):
        with open(config_file) as f:
            config = json.load(f)
            cells = []
            for cell_config in config['cells']:
                cell = CellFactory.create_cell(cell_config)
                cells.append(cell)
            print(cells)
            return cells
