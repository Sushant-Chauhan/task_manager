Used for tracking major updates, changes, and releases:  

### [0.1.0] - 2025-03-25
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
python manage.py migrate  #Apply Migrations- create tables: users, admin logs, sessions
python manage.py createsuperuser  #My cred-  username : sushant, password : 1234
python manage.py runserver     #Run the Server 
```

- Initial release of Task Management API.
```markdown
1: Define Models - User, Task 
2: Register Models in Admin Panel
3: Created,Apply Migrations - python manage.py makemigrations ;  python manage.py migrate
4 : Wrote Serializers for Models in tasks/serializers.py 
5 : Created Views in tasks/views.py (create, assign and retrieve tasks APIs)
6: Configured URLs in tasks/urls.py
7 : Include Project Level URLs in the main task_manager/urls.py
8: Tested APIs by running server - python manage.py runserver
    - Create a Task with Endpoint: POST /api/tasks/create/ 
    - Assign Users to a Task with Endpoint: POST /api/tasks/1/assign/
    - Retrieve Tasks for a User with Endpoint: GET /api/users/1/tasks/
```

