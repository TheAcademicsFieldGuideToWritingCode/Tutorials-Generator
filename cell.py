from abc import ABC, abstractmethod
from cell_type import CellType

class Cell(ABC):
    def __init__(self, prompt: str, cell_type: CellType, content: str):
        self.prompt = ""
        self.cell_type = cell_type
        self.context = None
        self.content = content


    def set_context(self, context_cell):
        self.context = context_cell

    def set_content(self, content: str):
        self.content = content

    @abstractmethod
    def generate_prompt(self):
        pass