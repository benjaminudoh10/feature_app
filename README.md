# Feature Request App

Feature Request App is a web application that allows the user to create "feature requests".
It was built with the Flask Web Framework

## Tools
* **Flask**

* **SQL-Alchemy**

* **Flask-SqlAlchemy**

* **SemanticUI**

* **JQuery**

### Usage:

1. Fetch repository, `git clone https://github.com/benjaminudoh10/Feature_Request_App.git`

2. `cd Feature_Request_App`

3. Install dependencies from requirements.txt `pip install -r requirements.txt`

4. Initialize database migrations `flask db init`

6. Migrate Database `flask db migrate`

7. Upgrade Database `flask db upgrade`

5. run flask server `flask run`

6. Visit Landing Page at http://localhost:5000/

7. Run tests `python tests.py`

## Deployment
This application was deployed to pythonanywhere.com which has servers that run on Ubuntu. It was deployed by cloning the application from the current repository on github and setting up the database.

>Visit http://adeyinka.pythonanywhere.com/ to view the current landing page of this project.
