from typing import Any
from uuid import UUID
from datetime import datetime

def format_data(data: dict[str, Any]) -> dict[str, Any]:
    attributes = {}
    for k, v in data.items():
        if isinstance(v, UUID):
            attributes[k] = str(v)
        elif isinstance(v, datetime):
            attributes[k] = v.isoformat()
        elif isinstance(v, dict):
            attributes[k] = format_data(v)
        elif isinstance(v, list):
            attributes[k] = list(map(lambda x: format_data(x), v))
        else:
            attributes[k] = v

    return attributes