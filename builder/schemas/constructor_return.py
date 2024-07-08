from pydantic import BaseModel


class ConstructorReturn:
    
    def __init__(self, name: str, diagrams: dict[str, BaseModel]) -> None:
        self.name = name
        self.diagrams = diagrams

    def get_data(self) -> dict[str, BaseModel]:
        return {k: v for k, v in self.diagrams.items()}