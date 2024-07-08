from builder.schemas import DiagramScheme, ConstructorReturn
from pydantic import BaseModel


class Constructor:

    def construct(self, name, diagrams: dict[DiagramScheme]) -> ConstructorReturn:
        classes = []
        for k, diagram in diagrams.items():
            classes.append(self._construct(name, diagram))
        data = {
            'name': name,
            'diagrams': {
                self.get_name(name=name, class_name=_class.__name__): _class for _class in classes
                }
            }
        return ConstructorReturn(**data)
    
    def _construct(self, name, diagram: DiagramScheme) -> BaseModel:
        return type(
            f'{name}{diagram.__class__.__name__}',
            (BaseModel, ),
            diagram.get_data()
            )
    
    def get_name(self, name: str, class_name: str) -> str:
        return class_name.replace(name, '').lower()
        
