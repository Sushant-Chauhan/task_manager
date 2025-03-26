This is generally used for tracking major updates, changes, and releases. Example:  

```markdown
# Changelog

## [0.1.0] - 2025-03-25

- Initial setup
```bash
mkdir task_manager
cd task_manager
python -m venv env
env\Scripts\activate
pip install django djangorestframework  #Install Django and Django REST Framework
django-admin --version
django-admin startproject task_manager .    #Create the Django Project inside same task_manager folder only (creates task_manager folder with 5 .py files - asgi, settings, urls, wsgi, __init__)
python manage.py startapp tasks  #Create the App  (Generates 1 Folder tasks/ on Root level which contains migrations folder and 6 .py files i.e. _init_ , admin, apps, models, tests, views ;  manage.py on Root level ; __pycache__ Folder inside task_manager Folder)
created requirements.txt, README.md, CHANGELOG.md, .gitignore

python manage.py runserver  #Apply Migrations- create tables: users, admin logs, sessions

python manage.py runserver     #Run the Server

 
```


- Initial release of Task Management API.

- Implemented task creation, assignment, and retrieval endpoints.

## [0.2.0] - 2025-03-26
- Improved API error handling.
- Added validation for task assignment.
