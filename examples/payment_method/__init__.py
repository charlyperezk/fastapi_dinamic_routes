from router_manager import utils, db, Entity
import router_manager.controller.route_manager as control
from examples.payment_method.model import PaymentMethod
from examples.payment_method.schemas import classes


__name__ = "payment_method"

try:
    from examples.database import get_session

    entity = Entity(
        db_model=PaymentMethod,
        **classes.get_data()
    )

    session = get_session()
    crud_client = db.CRUDController(model=entity.db_model)
except Exception as e:
    raise utils.exc.InitializationError(f"Error initializing {__name__}. Details: {e}")


route_manager = control.RouteManager(__name__,
                            entity,
                            crud_client,
                            session
                            )