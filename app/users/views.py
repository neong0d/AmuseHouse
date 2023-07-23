from rest_framework.generics import (
    CreateAPIView,
)

from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer