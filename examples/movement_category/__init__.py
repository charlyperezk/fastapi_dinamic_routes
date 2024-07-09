from router_manager import utils, db, Entity
import router_manager.controller.route_manager as control
from examples.movement_category.model import MovementCategory
from examples.movement_category.schemas import classes


__name__ = "movement_category"

try:
    from examples.database import get_session

    entity = Entity(
        db_model=MovementCategory,
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