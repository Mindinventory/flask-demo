# flask-demo

## Prerequisites
- Python 3.10 or greater versions
- MySql
- Install Pipenv
- Creating a virtual python environment dedicated for this application is strongly recommended to prevent your local system from breaking unexpectedly.
- Before taking the pull, create folder name .venv in your current Directory
- Virtual Environment Folder will have all the dependencies installed locally and With Your Current Directory name will be created

### Recommended tools
- PyCharm : Text Editor for Python 
- Visual Studio
- phpmyadmin, Adminer : For Sql

### Setting up
* To create tables in database:
  - run ```flask db migrate -m "Initial migration."``` to generate initial migrations. 
  - run ```flask db upgrade``` to apply migrations to the database

### Run Python server
- python run.py or flask run

## Project Structure
```
├── config
│   └── config.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 0ee6e1fd82ba_initial_migration.py
├── README.md
├── requirements.txt
├── run.py
└── src
    ├── api
    │   ├── __init__.py
    │   └── v1
    │       └── user
    │           ├── endpoints.py
    │           ├── __init__.py
    │           └── models.py
    ├── app.py
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   └── model.py
    └── routes
        ├── __intit__.py
        └── route.py
```