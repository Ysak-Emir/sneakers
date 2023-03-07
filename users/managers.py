from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, full_name, email, phone, password, avatar, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            full_name=full_name,
            avatar=avatar,
            email=email,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, full_name, email, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        email = self.normalize_email(email)
        user = self.model(
            full_name=full_name,
            email=email,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)

        user.save()

        return user
