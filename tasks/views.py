from django.shortcuts import render

# ----  CREATING VIEWS here -------


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Task
from .serializers import TaskSerializer, UserSerializer

# API to Create a Task
class TaskCreateAPIView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task created successfully", "task": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API to Assign a Task to Users
class TaskAssignAPIView(APIView):
    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_ids = request.data.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)

        if not users:
            return Response({"error": "No valid users found"}, status=status.HTTP_400_BAD_REQUEST)
        
        task.assigned_users.add(*users)
        return Response({"message": "Users assigned to the task successfully"}, status=status.HTTP_200_OK)

# API to Get Tasks for a Specific User
class UserTaskListAPIView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"user": UserSerializer(user).data, "tasks": serializer.data}, status=status.HTTP_200_OK)
