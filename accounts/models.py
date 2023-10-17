from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,BaseUserManager,PermissionsMixin

import phonenumbers

class CustomeBaseUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number field must be set')

        # Normalize the phone number
        normalized_phone_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(normalized_phone_number):
            raise ValueError('Invalid phone number')

        normalized_phone_number = phonenumbers.format_number(normalized_phone_number, phonenumbers.PhoneNumberFormat.E164)

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user = self.model(phone_number=normalized_phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone_number, password, **extra_fields)



class CustomeUser(AbstractBaseUser, PermissionsMixin):
    username  = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomeBaseUserManager()

    def __str__(self):
        return self.phone_number