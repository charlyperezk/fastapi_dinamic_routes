from builder.box.box import Box
from builder.schemas import DiagramScheme


class DiagramsBox(Box[DiagramScheme]):
    def __init__(self, diagrams: tuple[DiagramScheme]):
        super().__init__("DiagramsBox")
        self._box_content = {i: diagram() for i, diagram in enumerate(diagrams)}

