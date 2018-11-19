# CategoriesAPI

CategoriesAPI application can be used by two endpoints:
- ".../categories" can be used for putting JSON data to DB. Only "PUT" HTTP method allowed.
- ".../categories/<id>" can be used for getting data from DB. Only "GET" HTTP method allowed.

First of all you should create virtual environment for proper and more agile use of application.
Application was maintained on _virtualenv_ with _python3_ on it.

After virtualenv installed - install all application dependency modules using requirements.txt file.

For valid DB initialization and migrations you need to configure application:

```export FLASK_APP=run.py```

```flask db init```

```flask db migrate```

You can run application using:

```python run.py```
