from builder.schemas import BuilderScheme, DiagramScheme, ConstructorReturn
from builder.diagrammer import Diagrammer
from builder.constructor import Constructor


class Builder:
    def __init__(self, diagrams: tuple[DiagramScheme]) -> None:
        self.diagrammer = Diagrammer(diagrams)
        self.constructor = Constructor()

    def build(self, scheme: BuilderScheme) -> ConstructorReturn:
        fields = scheme.get_fields(scheme)
        diagrams = self.diagrammer.model(fields)
        classes = self.constructor.construct("User", diagrams)
        return classes