from django.db import models

# User Model
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

# Task Model
class Task(models.Model):
    TASK_STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    task_type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='Pending')
    
    # Many-to-Many relationship (Task can be assigned to multiple users)
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name
