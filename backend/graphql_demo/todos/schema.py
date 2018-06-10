import graphene

from graphene_django_extras import DjangoSerializerMutation, DjangoObjectType, DjangoInputObjectType

from graphql_demo.todos import models as todo_models
from graphql_demo.todos import serializers as todo_serializers
from graphql_demo.todos import api as todo_api

from graphql_jwt.decorators import login_required


class TodoType(DjangoObjectType):
    class Meta:
        model = todo_models.Todo


class TodoListType(DjangoObjectType):
    class Meta:
        model = todo_models.TodoList


class TodoListInputType(DjangoInputObjectType):
    class Meta:
        model = todo_models.TodoList


class TodoInputType(DjangoInputObjectType):
    class Meta:
        model = todo_models.Todo


class Queries(object):
    todo = graphene.Field(
        TodoType,
        id=graphene.Int(),
    )
    all_todos = graphene.List(TodoType)

    todo_list = graphene.Field(
        TodoListType,
        id=graphene.Int(),
    )
    all_todo_lists = graphene.List(TodoListType)

    def resolve_todo(self, info, **kwargs):
        todo_id = kwargs.get('id')

        if todo_id is not None:
            return todo_models.Todo.objects.get(pk=todo_id)

        return None

    def resolve_todo_list(self, info, **kwargs):
        todo_list_id = kwargs.get('id')

        if todo_list_id is not None:
            return todo_models.TodoList.objects.get(pk=todo_list_id)

        return None

    @login_required
    def resolve_all_todos(self, info, **kwargs):
        return todo_models.Todo.objects.all()

    @login_required
    def resolve_all_todo_lists(self, info, **kwargs):
        return todo_models.TodoList.objects.all()


class CreateTodo2(DjangoSerializerMutation):
    class Meta:
        serializer_class = todo_serializers.TodoSerializer


class CreateTodo(graphene.Mutation):
    """
         On traditional mutation classes definition you must implement the mutate function

    """

    todo_list = graphene.Field(TodoListType, required=False)
    ok = graphene.Boolean()

    class Arguments:
        new_todo = graphene.Argument(TodoInputType)

    class Meta:
        description = " Graphene traditional mutation for TodoList "

    def mutate(self, info, *arg, **kwargs):
        user = info.context.user
        creator = None
        if not user.is_anonymous:
            creator = user

        todo = todo_api.create_todo(
            description=kwargs['new_todo']['description'],
            todo_list=todo_models.TodoList.objects.get(pk=kwargs['new_todo']['todolist']),
            creator=creator,
        )
        ok = True

        return CreateTodo(todo=todo, ok=ok)


class UpdateTodo(graphene.Mutation):
    """
         On traditional mutation classes definition you must implement the mutate function

    """

    todo = graphene.Field(TodoType, required=False)
    ok = graphene.Boolean()

    class Arguments:
        todo_id = graphene.Int()
        todo = graphene.Argument(TodoInputType)

    class Meta:
        description = "Update mutation for Todo"

    def mutate(self, info, *arg, **kwargs):
        finished = False
        if not kwargs['todo']['finished_at']:
            finished = kwargs['todo']['finished_at']
        todo = todo_models.TodoList.objects.get(pk=kwargs['todo_id'])
        todo = todo_api.update_todo(
            todo,
            description=kwargs['todo']['description'],
            finished=finished
        )
        ok = True

        return UpdateTodo(todo=todo, ok=ok)


class DeleteTodo(graphene.Mutation):
    """
         On traditional mutation classes definition you must implement the mutate function

    """

    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        todo_id = graphene.Int()

    class Meta:
        description = " Graphene traditional mutation for TodoList "

    def mutate(self, info, *arg, **kwargs):
        todo_models.Todo.objects.get(pk=kwargs['todo_id']).delete()
        ok = True

        return DeleteTodo(id=kwargs['todo_id'], ok=ok)


class CreateTodoList(graphene.Mutation):
    """
         On traditional mutation classes definition you must implement the mutate function

    """

    todo_list = graphene.Field(TodoListType, required=False)
    ok = graphene.Boolean()

    class Arguments:
        new_todo_list = graphene.Argument(TodoListInputType)

    class Meta:
        description = " Graphene traditional mutation for TodoList "

    def mutate(self, info, *arg, **kwargs):
        user = info.context.user
        creator = None
        if not user.is_anonymous:
            creator = user

        print(kwargs)
        todo_list = todo_api.create_todo_list(title=kwargs['new_todo_list']['title'], creator=creator)
        ok = True

        return CreateTodoList(todo_list=todo_list, ok=ok)


class UpdateTodoList(graphene.Mutation):
    """
         On traditional mutation classes definition you must implement the mutate function

    """

    todo_list = graphene.Field(TodoListType, required=False)
    ok = graphene.Boolean()

    class Arguments:
        todo_list_id = graphene.Int()
        todo_list = graphene.Argument(TodoListInputType)

    class Meta:
        description = " Graphene traditional mutation for TodoList "

    def mutate(self, info, *arg, **kwargs):
        todo_list = todo_models.TodoList.objects.get(pk=kwargs['todo_list_id'])
        todo_list = todo_api.update_todo_list(
            todo_list,
            title=kwargs['todo_list']['title'],
            creator=kwargs['todo_list']['creator'],
        )
        ok = True

        return UpdateTodoList(todo_list=todo_list, ok=ok)


class DeleteTodoList(graphene.Mutation):
    """
         On traditional mutation classes definition you must implement the mutate function

    """

    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        todo_list_id = graphene.Int()

    class Meta:
        description = " Graphene traditional mutation for TodoList "

    def mutate(self, info, *arg, **kwargs):
        todo_models.TodoList.objects.get(pk=kwargs['todo_list_id']).delete()
        ok = True

        return DeleteTodoList(id=kwargs['todo_list_id'], ok=ok)


class Mutations(graphene.ObjectType):
    # Todo mutations
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
    # TodoList mutations
    create_todo_list = CreateTodoList.Field()
    update_todo_list = UpdateTodoList.Field()
    delete_todo_list = DeleteTodoList.Field()
    # Out of the box mutations
    create_todo2 = CreateTodo2.CreateField()
    update_todo2 = CreateTodo2.UpdateField()
    delete_todo2 = CreateTodo2.DeleteField()
