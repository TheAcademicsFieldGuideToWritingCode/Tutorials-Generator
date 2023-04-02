from cell import Cell
from cell_type import CellType


class KnowledgeTestingCell(Cell):
    def __init__(
        self, n: int, question_type: str, target_audience: str, topic: str, cell_type, context, type='KnowledgeTestingCell'
    ):
        self.n = n
        self.question_type = question_type
        self.target_audience = target_audience
        self.topic = topic
        self.cell_type = CellType[cell_type.upper()]
        self.context = None
        self.content = ""
        self.prompt = ""
        self.type = type

    def generate_prompt(self):
        if self.cell_type == CellType.MARKDOWN:
            return f"Design {self.n} {self.question_type} of an appropriate difficulty for {self.target_audience} about that {self.topic}"
        else:
            try:
                prompt = f"Create code with empty methods that have comments for what they should do but no implementation to answer the following question: {self.context.content}. After that, create 3 assertions tests that the student will use to test if they have implemented their code correctly. Produce output that goes directly in a jupyter notebook code cell."
                return prompt
            except:
                return f"failed"
