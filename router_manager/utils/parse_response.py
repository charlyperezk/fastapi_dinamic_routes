from typing import Any
from uuid import UUID

def format_data(data: dict[str, Any]) -> dict[str, Any]:
    attributes = {}
    for k, v in data.items():
        if isinstance(v, UUID):
            attributes[k] = str(v)
        else:
            attributes[k] = v
    return attributes