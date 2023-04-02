from cell import Cell, CellType


class ExplanatoryCell(Cell):
    """
    A class representing an explanatory cell in a Jupyter Notebook.
    """

    def __init__(self, topic, method_of_teaching, target_audience, cell_type, context, type='ExplanatoryCell'):
        """
        Initialize a new ExplanatoryCell object.

        Args:
            topic (str): The topic of the explanatory cell.
            method_of_teaching (str): The method of teaching to use in the explanatory cell.
            cell_type (CellType): The type of the explanatory cell.
        """
        self.topic = topic
        self.method_of_teaching = method_of_teaching
        self.target_audience = target_audience
        self.context = None
        self.cell_type = CellType[cell_type.upper()]
        self.prompt = self.generate_prompt()
        self.content = ""
        self.type = type

    def generate_prompt(self):
        """
        Generate the prompt for the ExplanatoryCell.

        Returns:
            str: The prompt for the ExplanatoryCell.
        """
        type_of_cell = "Markdown" if self.cell_type == CellType.MARKDOWN else "Code"
        return f"This is a {type_of_cell} cell in a Jupyter Notebook use appropriate headers for chapter sections if of type markdown. Explain {self.topic} by {self.method_of_teaching}."
