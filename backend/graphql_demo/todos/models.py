from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    title = models.CharField(max_length=128, default='untitled')
    created_at = models.DateField(auto_now=True)
    creator = models.ForeignKey(User, null=True, blank=True, related_name='todo_lists', on_delete=models.CASCADE)


class Todo(models.Model):
    description = models.CharField(max_length=256)
    created_at = models.DateField(auto_now=True)
    finished_at = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, null=True, related_name='todos', on_delete=models.CASCADE)
    todolist = models.ForeignKey(TodoList, related_name='todos', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
