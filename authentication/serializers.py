from rest_framework import serializers
from .models import User
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """

    def create(self, validated_data):  
        if validated_data.get('date_of_birth') is None:
            raise serializers.ValidationError("Date of birth is required.")
        
        today = date.today()
        birth_date = validated_data['date_of_birth']
        age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day)
        )            
        if age < 15:
            raise serializers.ValidationError("User must be at least 15 years old.")             

        return User.objects.create_user(**validated_data)

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
