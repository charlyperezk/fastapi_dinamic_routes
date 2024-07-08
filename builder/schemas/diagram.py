from builder.schemas.field import Field, FieldVisibility
from builder.box.config.attributes import AttrsBox
from typing import Any


class DiagramScheme:
    _visibility: set[FieldVisibility] = ...

    def __init__(self):
        self._attributes_box = AttrsBox()

    def add_field(self, field: Field):
        self._attributes_box.save_attribute(field.to_attribute())

    def get_attributes(self) -> dict[str, Any]:
        attributes = {}
        for k, v in self._attributes_box._box_content.items():
            if v["value"] is not None:
                attributes[k] = v['value']
        return attributes

    def get_annotation(self) -> dict[str, Any]:
        return {k: v['type'] for k, v in self._attributes_box._box_content.items()}
                    
    def get_data(self) -> dict[str, Any]:
        return {
            "__annotations__": self.get_annotation(),
            **self.get_attributes()
            }

class Create(DiagramScheme):
    _visibility = {FieldVisibility.DELETE}
    
class Read(DiagramScheme):
    _visibility = {FieldVisibility.READ}

class Update(DiagramScheme):
    _visibility = {FieldVisibility.UPDATE}
