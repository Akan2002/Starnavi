from mainapp.models import(
    User, SmsUser,
)
from rest_framework import serializers, exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'name', 'surname', 'age',
        )
class SmsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsUser
        fields = (
            'id', 'message',
        )
class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 8:
            raise exceptions.ValidationError('Password is to short')
        elif len(value) > 8:
            raise exceptions.ValidationError('Password is to long')
        return value
class AuthorizationSeriaizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()