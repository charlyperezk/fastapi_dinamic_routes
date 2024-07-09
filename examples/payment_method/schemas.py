from pydantic.types import UUID4
from builder import Builder
from builder.schemas import Field, FieldVisibility as Visibility, BuilderScheme, Read, Update, Create, Admin


class PaymentMethodBuild(BuilderScheme):
    __scheme_name__ = "PaymentMethod"
    id = Field(UUID4, visibility={Visibility.READ})
    name = Field(str, visibility={Visibility.ALL})
    description = Field(str, visibility={Visibility.ALL})
    default = Field(bool, False, visibility={Visibility.ADMIN})

builder = Builder(diagrams=(Read, Update, Create, Admin))
classes = builder.build(scheme=PaymentMethodBuild)