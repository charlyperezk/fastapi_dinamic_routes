from datetime import datetime
from pydantic.types import UUID4
from builder import Builder
from builder.schemas import Field, FieldVisibility as Visibility, BuilderScheme, Read, Update, Create, Admin
from routes.movement.schemas import classes as MovementClasses


class AccountBuild(BuilderScheme):
    __scheme_name__ = "Account"
    id = Field(UUID4, visibility={Visibility.READ})
    created_at = Field(datetime, visibility={Visibility.READ})
    name = Field(str, visibility={Visibility.ALL})
    description = Field(str, visibility={Visibility.ALL})
    movements = Field(list[MovementClasses.get_data()['read']], visibility={Visibility.READ})

builder = Builder(diagrams=(Read, Update, Create, Admin))
classes = builder.build(scheme=AccountBuild)