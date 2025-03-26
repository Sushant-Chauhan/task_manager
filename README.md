# Task Management API

## 📌 Project Overview
This is a simple Task Management API built using **Django** and **Django REST Framework**. It allows users to:
- Create tasks
- Assign tasks to multiple users
- Retrieve tasks assigned to a specific user

## Tech Stack
- Python
- Django
- Django Rest Framework
- SQLite (Default Database)


## API Endpoints
```bash
POST /api/tasks/create/ - Create a Task
POST /api/tasks/{id}/assign/ - Assign a Task
GET /api/users/{user_id}/tasks/ - Retrieve Tasks for a User
```


## Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/task_manager.git
cd task_manager
```

2. **Create and Activate Virtual Environment**

```bash
python -m venv env
env\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Migrations**
```bash
python manage.py migrate
```

5. **Create Superuser**
```bash
python manage.py createsuperuser
```

6. **Start the Server**
```bash
python manage.py runserver
```