from builder.schemas import DiagramScheme, Field, FieldVisibility as vis
from builder.box.config.diagrams import DiagramsBox


class Diagrammer:

    def __init__(self, diagrams: tuple[DiagramScheme]):
        self.diagrams_box: DiagramsBox = DiagramsBox(diagrams)

    def model(self, fields: tuple[Field]) -> dict[int, DiagramScheme]:
        for diagram in self.diagrams_box.content:
            for field in fields:
                for f_visibility in field._visibility:
                    if f_visibility == vis.ALL:
                        diagram.add_field(field)
                    else:
                        for d_visibility in diagram._visibility:
                            if f_visibility == d_visibility:
                                diagram.add_field(field)
        return self.diagrams_box._box_content
