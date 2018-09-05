from rest_framework import serializers

from graphql_demo.todos import models as todos_models


class TodoSerializer(serializers.ModelSerializer):
    finished_at = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = todos_models.Todo
        fields = ("description", "created_at", "assigned_to", "todolist", "finished_at")


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = todos_models.TodoList
        fields = "__all__"
