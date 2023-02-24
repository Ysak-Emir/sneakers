from django.db import models
from django.core.validators import FileExtensionValidator
from users.avatar_setting_file import get_path_upload_avatar
from products.models import Product


class Account(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    number = models.IntegerField(unique=True)
    password = models.CharField(max_length=255)
    login = models.CharField(max_length=100, unique=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


class Favorite(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    products_id = models.ForeignKey(Product, on_delete=models.CASCADE)
