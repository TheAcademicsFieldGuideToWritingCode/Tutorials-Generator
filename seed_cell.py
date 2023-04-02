from cell import Cell
from cell_type import CellType

class SeedCell(Cell):
    def __init__(self, identity: str, topic: str, target_audience: str, type='SeedCell'):
        self.identity = identity
        self.topic = topic
        self.target_audience = target_audience
        self.type = type
        super().__init__(self.generate_prompt(), CellType.MARKDOWN, content = "")

    def generate_prompt(self):
        return f"Behave as a {self.identity} who is explaining {self.topic} to {self.target_audience}"
