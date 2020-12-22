# Couch Watch
A simple app to browse, list of shows on Netflix using fastapi. This app uses fastapi, sqlalchemy relationships and 
sqlite database to create a nice demo app that covers edge cases. The frontend is a very simple HTMLResponse and
user Bulma CSS and JQuery Datatables for the table.

- Live URL: https://couchwatch.uc.r.appspot.com/
- API Docs: https://couchwatch.uc.r.appspot.com/docs
- Alt Docs: https://couchwatch.uc.r.appspot.com/redoc

# Screenshots
![Alt text](home.png?raw=true "Home Page")

![Alt text](swagger.png?raw=true "Swagger Docs")

![Alt text](redoc.png?raw=true "Redoc")

# Installation
* Make sure you have `python` installed. Check with 
    ```
    python --version
    ```
* Install `pipenv`
    ```
    curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python
    ```
* Activate Virtual Environment 
    ```
    pipenv shell
    ```
* Install Dependencies 
    ```
    pipenv install
    ```
* Run Development Server (uvicorn)
    ```
    uvicorn main:app --reload
    ```
* Import sample data from the sample_data.csv
    ```
    python import_data.py
    ```
* Navigate to the URL in a web browser
    - Frontend: http://localhost:8000/
    - API Docs: http://localhost:8000/docs/
    - Alternate API Docs: http://localhost:8000/redoc/
    
# TODO
- Edit/Update Functionality
- Detail Page for each Show? Support for cover image?
- API Authentication using JWT: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- Proper Environments for Dev, QA and Prod: https://fastapi.tiangolo.com/advanced/settings/
- Large CSV Import through UI possibly using pandas? https://www.kaggle.com/szelee/how-to-import-a-csv-file-of-55-million-rows


# References
- https://fastapi.tiangolo.com/tutorial/bigger-applications/
- https://fastapi.tiangolo.com/python-types/
- https://bulma.io/documentation/elements/table/
- https://datatables.net/examples/styling/bulma.html
- https://medium.com/analytics-vidhya/deploying-fastapi-application-in-google-app-engine-in-standard-environment-dc061d3277a
- https://baskus.wordpress.com/2019/09/29/how-to-deploy-to-app-engine-using-github-actions/
- https://dev.to/mungell/google-cloud-app-engine-environment-variables-5990
- https://cloud.google.com/iam/docs/granting-changing-revoking-access