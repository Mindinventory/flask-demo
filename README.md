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
- python run.py

## Project Structure
```
├── config
│   ├── config.py
│   └── logger.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── README.md
├── requirements.txt
├── run.py
└── src
    ├── api
    │   ├── __init__.py
    │   └── v1
    │       ├── auth
    │       │   ├── controller.py
    │       │   ├── crud.py
    │       │   ├── __init__.py
    │       │   ├── route.py
    │       │   └── schema.py
    │       └── user
    │           ├── controller.py
    │           ├── crud.py
    │           ├── __init__.py
    │           ├── models.py
    │           ├── route.py
    │           └── schema.py
    ├── db
    │   └── session.py
    ├── general
    │   ├── hash_utils.py
    │   ├── helper.py
    │   ├── __init__.py
    │   ├── message.json
    │   ├── response.py
    │   └── token_utils.py
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   └── model.py
    └── routes
        ├── __init__.py
        └── route.py
```