from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'date_of_birth',
            'can_be_contacted',
            'can_data_be_shared',
            'age'
        ]
        read_only_fields = ['id', 'age']
