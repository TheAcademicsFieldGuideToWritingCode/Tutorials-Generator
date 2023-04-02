from cell import Cell
from seed_cell import SeedCell
from explanatory_cell import ExplanatoryCell
from knowledge_testing_cell import KnowledgeTestingCell

class CellFactory:
    CELL_TYPES = {
        'SeedCell': SeedCell,
        'ExplanatoryCell': ExplanatoryCell,
        'KnowledgeTestingCell': KnowledgeTestingCell,
    }
    
    @staticmethod
    def create_cell(cell_config):
        cell_type = cell_config['type']
        cell_class = CellFactory.CELL_TYPES.get(cell_type)
        if not cell_class:
            raise ValueError(f"Invalid cell type: {cell_type}")
        return cell_class(**cell_config)

