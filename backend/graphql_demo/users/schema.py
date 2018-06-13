import graphene

from django.contrib.auth.models import User

from graphene_django_extras import (
    DjangoListObjectType,
    DjangoObjectType,
    DjangoFilterListField,
    DjangoSerializerMutation,
)
from graphene_django_extras.paginations import LimitOffsetGraphqlPagination

import graphql_jwt


from graphql_demo.users import serializers as users_serializers


class UserType(DjangoObjectType):
    class Meta:
        model = User
        description = " Type definition for a single user "
        filter_fields = {
            "id": ["exact"],
            "first_name": ["icontains", "iexact"],
            "last_name": ["icontains", "iexact"],
            "username": ["icontains", "iexact"],
            "email": ["icontains", "iexact"],
        }


class UserListType(DjangoListObjectType):
    class Meta:
        description = " Type definition for user list "
        model = User
        # ordering can be: string, tuple or list
        pagination = LimitOffsetGraphqlPagination(
            default_limit=25, ordering="-username"
        )


class UserSerializerMutation(DjangoSerializerMutation):
    """
        DjangoSerializerMutation auto implement Create, Delete and Update functions
    """

    class Meta:
        description = " DRF serializer based Mutation for Users "
        serializer_class = users_serializers.UserSerializer


class Queries(graphene.ObjectType):
    all_users = DjangoFilterListField(UserType)
    user = UserListType.RetrieveField(
        description="User List with pagination and filtering"
    )


class Mutations(graphene.ObjectType):
    create_user = UserSerializerMutation.CreateField()
    update_user = UserSerializerMutation.UpdateField()
    delete_user = UserSerializerMutation.DeleteField()
    # JWT authentication
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
