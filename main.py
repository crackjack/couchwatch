
from fastapi import FastAPI, File, UploadFile
from db import sqlite_engine
from entries import routes as entry_routes
from entries import schemas as entry_schemas

from utils import convert_bytes_to_json_string

app = FastAPI()

# include module routes
app.include_router(entry_routes.router)

# create tables for modules
entry_schemas.Base.metadata.create_all(bind=sqlite_engine)


@app.get("/")
def ping():
    return {"status": "It Works!"}


@app.post("/upload/")
async def csv_to_json(file: UploadFile = File(...)):
    contents = await file.read()
    json_string = convert_bytes_to_json_string(contents)
    return {"data": json_string}

# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
