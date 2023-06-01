from abc import ABC, abstractmethod
from curriculum_module_generator.cell_type import CellType


class Block(ABC):
    def __init__(self, cell_type: CellType, content: str = "", context=None, type="Base"):
        self.cell_type = cell_type
        self.context = context
        self.content = content
        self.type = type

    def set_context(self, context_block):
        self.context = context_block

    def set_content(self, content: str):
        self.content = content

    @abstractmethod
    def generate_prompt(self) -> str:
        pass



class SeedBlock(Block):
    def __init__(self, identity: str, topic: str, target_audience: str, context=None, type="SeedBlock"):
        self.identity = identity
        self.topic = topic
        self.target_audience = target_audience
        super().__init__(CellType.MARKDOWN, type=type)

    def generate_prompt(self) -> str:
        return f"Behave as a {self.identity} who is explaining {self.topic} to {self.target_audience}"


class ExplanatoryBlock(Block):
    def __init__(
        self,
        topic: str,
        method_of_teaching: str,
        target_audience: str,
        cell_type: str,
        context=None,
        type="ExplanatoryBlock"
    ):
        self.topic = topic
        self.method_of_teaching = method_of_teaching
        self.target_audience = target_audience
        super().__init__(CellType[cell_type.upper()], type=type)

    def generate_prompt(self) -> str:
        type_of_cell = (
            "Markdown" if self.cell_type == CellType.MARKDOWN else "Code"
        )
        return f"This is a {type_of_cell} block in a Jupyter Notebook. Use appropriate headers for chapter sections if of type Markdown. Explain {self.topic} by {self.method_of_teaching} in a way that is relatable to {self.target_audience}. Be careful not to be overly dramatic and not to talk down to the audience regardless of their level of expertise."


class KnowledgeTestingBlock(Block):
    def __init__(
        self,
        n: int,
        question_type: str,
        target_audience: str,
        topic: str,
        cell_type: str,
        context=None,
        type="KnowledgeTestingBlock"
    ):
        self.n = n
        self.question_type = question_type
        self.target_audience = target_audience
        self.topic = topic
        super().__init__(CellType[cell_type.upper()], type=type)

    def generate_prompt(self) -> str:
        if self.cell_type == CellType.MARKDOWN:
            return f"Design {self.n} {self.question_type} of an appropriate difficulty for {self.target_audience} about that {self.topic}"
        else:
            if self.context:
                return f"Create code with empty methods that have comments for what they should do but no implementation to answer the following question: {self.context.content}. After that, create 3 assertion tests that the student will use to test if they have implemented their"
