import uuid
from pydantic.types import UUID4
from builder import Builder
from builder.schemas import Field, FieldVisibility as Visibility, BuilderScheme, Read, Update, Create

### SCHEMES    
class UserBuild(BuilderScheme):
    __scheme_name__ = "User"
    id = Field(UUID4, visibility={Visibility.READ})
    name = Field(str, visibility=Visibility.ALL)
    age = Field(int, visibility={Visibility.ALL})
    # photos = Field(list[str], visibility={Visibility.READ})
    # is_active = Field(bool, visibility={Visibility.UPDATE})
    # is_admin = Field(bool, visibility={Visibility.UPDATE})

builder = Builder(diagrams=(Read, Update, Create))
classes = builder.build(scheme=UserBuild)