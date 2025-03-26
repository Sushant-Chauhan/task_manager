from django.urls import path
from .views import TaskCreateAPIView, TaskAssignAPIView, UserTaskListAPIView

urlpatterns = [
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/<int:task_id>/assign/', TaskAssignAPIView.as_view(), name='task-assign'),
    path('users/<int:user_id>/tasks/', UserTaskListAPIView.as_view(), name='user-tasks'),
]
