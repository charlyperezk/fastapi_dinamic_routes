from fastapi import FastAPI
from routes import db, user, movement_type, movement_category, payment_method, movement, account


app = FastAPI()
# app.include_router(
#     user.route_manager.crud_route,
#     tags=[user.__name__]
#     )
app.include_router(
    movement_type.route_manager.crud_route,
    tags=[movement_type.__name__]
    )
app.include_router(
    movement_category.route_manager.crud_route,
    tags=[movement_category.__name__]
    )
app.include_router(
    payment_method.route_manager.crud_route,
    tags=[payment_method.__name__]
    )
app.include_router(
    movement.route_manager.crud_route,
    tags=[movement.__name__]
    )
app.include_router(
    account.route_manager.crud_route,
    tags=[account.__name__]
    )


# from routes.start_config import first_config
app.on_event("startup")(db.create_db)
# app.on_event("startup")(first_config)
