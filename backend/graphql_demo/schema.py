import graphene

from graphene_django.debug import DjangoDebug

from graphql_demo.todos import schema as todo_schema
from graphql_demo.users import schema as users_schema


class RootQuery(todo_schema.Queries, users_schema.Queries, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="__debug")


class RootMutations(todo_schema.Mutations, users_schema.Mutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutations)
