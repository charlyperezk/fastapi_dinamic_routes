from builder.box.box import Box
from typing import Any, Dict, Optional, TypeVar, Union, Generic, List


G = TypeVar('G', str, bool, int, float, None)

class Attribute(Generic[G]):
    def __init__(self, name: str, value: Optional[G] = None, annotation: Optional[Any] = None):
        self._name = name
        self._value = value
        self._annotation = annotation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def value(self) -> G:
        return self._value

    @value.setter
    def value(self, value: G) -> None:
        self._value = value

    def get_data(self) -> Dict[str, Any]:
        return {
            'name': self._name,
            'default_value': self._value,
            'type': self._annotation
        }

class AttrsBox(Box[Attribute[Union[str, bool]]]):
    def __init__(self, name: str|None = "AttrsBox"):
        super().__init__(name)

    def save_attribute(self, attribute: Attribute) -> None:
        self._box_content[attribute.name] = {'value': attribute._value, 'type': attribute._annotation}

    # def get_attributes(self) -> Dict[str, Attribute[Union[str, bool]]]:
    #     return self._box_content