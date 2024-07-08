from fastapi import FastAPI
from examples import db, user


app = FastAPI()
app.include_router(
    user.route_manager.crud_route,
    tags=[user.__name__]
    )

app.on_event("startup")(db.create_db)