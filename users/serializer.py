from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from users.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = 'id avatar full_name email number login'.split()


class AccountValidateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(min_length=1, required=True)
    email = serializers.EmailField(required=True)
    number = serializers.IntegerField(min_value=999000000000, max_value=999999999999, required=True)
    password = serializers.CharField(min_length=8, required=True)
    login = serializers.CharField(required=True)
    avatar = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])],
        required=True
    )