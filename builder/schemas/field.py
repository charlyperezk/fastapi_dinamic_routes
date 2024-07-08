from dataclasses import dataclass
from builder.box.config.attributes import Attribute


@dataclass
class FieldVisibility:
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    ALL = "*"

class Field:
    _name: str

    def __init__(
            self,
            type: type,
            value: str = None,
            description: str = None,
            visibility: set[FieldVisibility] = FieldVisibility.ALL
            ):
        
        self._type = type
        self._value = value
        self._description = description
        self._visibility = visibility

    def to_attribute(self):
        return Attribute(self._name, self._value, self._type)
