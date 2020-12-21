from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from db import sqlite_engine
from entries import routes as entry_routes
from entries import schemas as entry_schemas

from utils import convert_bytes_to_json_string

app = FastAPI()

# include module routes
app.include_router(entry_routes.router)

# create tables for modules
entry_schemas.Base.metadata.create_all(bind=sqlite_engine)


@app.get(
    "/",
    response_class=HTMLResponse
)
def home():
    table_rows = """
        <tr>
            <td>Tiger Nixon</td>
            <td>System Architect</td>
            <td>Edinburgh</td>
            <td>61</td>
            <td>2011/04/25</td>
            <td>$320,800</td>
        </tr>
    """
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Welcome to Couch Watch</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css">
            <link rel="stylesheet" href="https://cdn.datatables.net/1.10.22/css/dataTables.bulma.min.css">
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
            <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
            <script defer src="https://use.fontawesome.com/releases/v5.14.0/js/all.js"></script>
            <script defer src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
            <script defer src="https://cdn.datatables.net/1.10.22/js/dataTables.bulma.min.js"></script>
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
