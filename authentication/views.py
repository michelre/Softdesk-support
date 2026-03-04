from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    ViewSet for User model.
    Allows CRUD operations on users.
    """

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
