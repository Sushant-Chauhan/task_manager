from rest_framework import serializers
from .models import User, Task

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    # Display users as name instead of just IDs in the response
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
