from fastapi import FastAPI
from routers.userRoutes import router
from routers.external_api_quey import external_api
from config.database import Base, engine

app = FastAPI()
app.title = "MatchMate"

app.include_router(external_api)
app.include_router(router)

Base.metadata.create_all(bind=engine)
"""
Creates tables in the database based on the declarative model defined in `Base`.

This line ensures that the necessary database tables are created before the application starts accepting requests.
"""
