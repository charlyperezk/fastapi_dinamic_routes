from router_manager import utils, db, Entity
import router_manager.controller.route_manager as control
from routes.movement_type.model import MovementType
from routes.movement_type.schemas import classes


__name__ = "movement_type"

try:
    from routes.database import get_session

    entity = Entity(
        db_model=MovementType,
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