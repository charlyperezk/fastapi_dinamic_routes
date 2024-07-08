from typing import Dict, TypeVar, Generic, List


T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, name: str):
        self._box_name = name
        self._box_content: Dict[str, T] = {}

    @property
    def name(self) -> str:
        return self._box_name

    @name.setter
    def name(self, name: str) -> None:
        self._box_name = name

    @property
    def content(self) -> List[T]:
        return list(self._box_content.values())
    
    @content.setter
    def content(self, content: List[T]) -> None:
        self._box_content = {i: item for i, item in enumerate(content)}

    def __getitem__(self, name: str) -> T:
        return self._box_content[name]
    
    def __setitem__(self, name: str, value: T) -> None:
        self._box_content[name] = value
