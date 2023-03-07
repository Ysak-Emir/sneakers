from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from users.models import Account
from rest_framework.serializers import ValidationError
from rest_framework.authtoken.models import Token
from phonenumber_field.serializerfields import PhoneNumberField


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = 'id avatar full_name email phone'.split()


class AccountValidateSerializer(serializers.Serializer):
    full_name = serializers.CharField(min_length=1, required=True)
    email = serializers.EmailField(required=True)
    phone = PhoneNumberField(required=True)
    avatar = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])],
        required=True
    )


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'phone', 'password', 'password2']

    def validate_email(self, email):
        email_exists = Account.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError('Email already taken!')
        return email

    def validate_phone(self, phone):
        if len(phone) == 13 and phone[1:].isdigit() and phone[:4] == '+996':
            return phone
        raise ValidationError('Phone is incorrect format')

    def save(self, *args, **kwargs):

        user = Account(
            email=self.validated_data['email'],
            phone=self.validated_data['phone'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password2 != password:
            raise ValidationError({password: "Passwords not match"})

        user.set_password(password)
        user.save()
        Cart.objects.create(user=user)
        return user
