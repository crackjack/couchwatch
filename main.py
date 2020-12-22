import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from db import sqlite_engine
from entries import routes as entry_routes
from entries import schemas as entry_schemas
import requests

from utils import convert_bytes_to_json_string

app = FastAPI()

# include module routes
app.include_router(entry_routes.router)

# create tables for modules
entry_schemas.Base.metadata.create_all(bind=sqlite_engine)

# Change the URL based on environment
BASE_URL = "http://localhost:8000" \
    if os.environ.get("DEBUG", "true").lower() == "true" \
    else "https://couchwatch.uc.r.appspot.com/"


@app.get(
    "/",
    response_class=HTMLResponse
)
def home():
    response = requests.get(f"{BASE_URL}/browse/")
    table_rows = """"""
    for entry in response.json():
        table_rows += f"""
            <tr>
                <td>{entry['show_id']}</td>
                <td>{entry['title']}</td>
                <td>{entry['type']}</td>
                <td>{entry['duration']}</td>
                <td>{entry['date_added']}</td>
                <td>{entry['release_year']}</td>
            </tr>
        """
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport"
                content="width=device-width, initial-scale=1">
            <title>Welcome to Couch Watch</title>
            <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css">
            <link rel="stylesheet"
                    href="https://cdn.datatables.net/1.10.22/css/dataTables.bulma.min.css">
        </head>
        <body>
            <section class="hero">
              <div class="hero-body">
                <div class="container">
                  <h1 class="title">
                    Couch Watch
                  </h1>
                  <h2 class="subtitle">
                    Netflix Movies and TV Shows
                  </h2>
                </div>
              </div>
            </section>
            <table id="shows" class="table is-striped is-fullwidth">
        <thead>
            <tr>
                <th>Show ID</th>
                <th>Title</th>
                <th>Type</th>
                <th>Duration</th>
                <th>Added date</th>
                <th>Year</th>
            </tr>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
        <tfoot>
            <tr>
                <th>Show ID</th>
                <th>Title</th>
                <th>Type</th>
                <th>Duration</th>
                <th>Added date</th>
                <th>Year</th>
            </tr>
        </tfoot>
    </table>
            <script
                src="https://code.jquery.com/jquery-3.5.1.js"></script>
            <script defer
                src="https://use.fontawesome.com/releases/v5.14.0/js/all.js"></script>
            <script defer
                src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
            <script defer
                src="https://cdn.datatables.net/1.10.22/js/dataTables.bulma.min.js"></script>
            <script type="text/javascript">
                $(document).ready(function() {{
                    $('#shows').DataTable();
                }});
            </script>
        </body>
    </html>
    """


@app.post("/upload/")
async def csv_to_json(file: UploadFile = File(...)):
    contents = await file.read()
    json_string = convert_bytes_to_json_string(contents)
    return {"data": json_string}

# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
