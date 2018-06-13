from django.utils import timezone

from graphql_demo.todos import models


def create_todo(description, todo_list, creator=None):
    return models.Todo.objects.create(
        description=description, creator=creator, todolist=todo_list
    )


def update_todo(todo, description=None, finished=False):
    if description:
        todo.description = description
    if finished:
        todo.finished_at = timezone.now()

    todo.save()
    return todo


def create_todo_list(title, creator=None):
    return models.TodoList.objects.create(title=title, creator=creator)


def update_todo_list(todo_list, title=None, creator=None):
    if title:
        todo_list.title = title
    if creator:
        todo_list.creator = creator

    todo_list.save()
    return todo_list
