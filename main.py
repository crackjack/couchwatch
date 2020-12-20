
from fastapi import FastAPI
from db import sqlite_engine
from entries import routes as entry_routes
from entries import models as entry_models

app = FastAPI()

# include module routes
app.include_router(entry_routes.router)

# create tables for modules
entry_models.Base.metadata.create_all(bind=sqlite_engine)


@app.get("/")
def ping():
    return {"status": "It Works!"}


# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
