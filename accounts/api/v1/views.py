from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from accounts.api.v1.serializers import UserSerializer
from rest_framework.authtoken.models import Token


@api_view(["POST"])
@permission_classes([])  # signup is not supposed to require user be authenticated first
def signup(request):

    data = {"data": "", "status": ""}
    user_serialized = UserSerializer(data=request.data)

    if user_serialized.is_valid():
        user_serialized.save()
        print(user_serialized.data)
        data["data"] = {
            "user": user_serialized.data,
            "token": Token.objects.get(
                user__username=user_serialized.data.get("username")
            ).key,
            "message": f"User '{user_serialized.data.get('username')}' created!",
        }

        data["status"] = status.HTTP_201_CREATED
    else:
        data["data"] = user_serialized.errors
        data["status"] = status.HTTP_400_BAD_REQUEST

    return Response(**data)


@api_view(["POST"])
def user_logout(request):
    """
    logout a user by deleting their token

    logout may be done by POST reques see:
    1. https://github.com/django/django/pull/12504
    2. https://github.com/django/django/blob/main/django/contrib/auth/views.py#L130

    """
    try:
        request.user.auth_token.delete()
    except Exception as e:
        print(e)

    logout(request)

    return Response(status.HTTP_200_OK)
