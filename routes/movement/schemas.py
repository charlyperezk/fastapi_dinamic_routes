from pydantic.types import UUID4
from builder import Builder
from builder.schemas import Field, FieldVisibility as Visibility, BuilderScheme, Read, Update, Create, Admin
from routes.payment_method import classes as PaymentMethodClasses
from routes.movement_type import classes as MovementTypeClasses
from routes.movement_category import classes as MovementCategoryClasses
from datetime import datetime


class MovementBuild(BuilderScheme):
    __scheme_name__ = "Movement"
    id = Field(UUID4, visibility={Visibility.READ})
    date = Field(datetime, datetime.now(), visibility={Visibility.ALL})
    id_payment_method = Field(UUID4, visibility={Visibility.CREATE})
    id_movement_type = Field(UUID4, visibility={Visibility.CREATE})
    id_movement_category = Field(UUID4, visibility={Visibility.CREATE})
    id_account = Field(UUID4, visibility={Visibility.CREATE})
    payment_method = Field(PaymentMethodClasses.get_data()['read'], visibility={Visibility.READ})
    movement_type = Field(MovementTypeClasses.get_data()['read'], visibility={Visibility.READ})
    movement_category = Field(MovementCategoryClasses.get_data()['read'], visibility={Visibility.READ})
    default = Field(bool, False, visibility={Visibility.ADMIN})

builder = Builder(diagrams=(Read, Update, Create, Admin))
classes = builder.build(scheme=MovementBuild)