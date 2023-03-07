from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField

class Account(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    phone = PhoneNumberField(unique=True)
    avatar = models.ImageField(
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


