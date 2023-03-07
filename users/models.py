from django.db import models
from django.core.validators import FileExtensionValidator
from products.models import Product
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import CustomUserManager


class Account(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    phone = PhoneNumberField(unique=True)
    avatar = models.ImageField(
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
    )
    objects = CustomUserManager()
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone', 'full_name']

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
