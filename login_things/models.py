from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email, nama, nik, password=None):
        if not email:
            raise ValueError("Tidak Ada Email yang Dimasukkan")
        if not password:
            raise ValueError("Tidak Ada Password yang Dimasukkan")
        if len(nik) != 16 and not nik.isnumeric():
            raise ValueError("NIK Tidak Valid")
        email = self.normalize_email(email)
        user = self.model(email=email, nama=nama, nik=nik)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nama, nik, password):
        user = self.create_user(email, nama, nik, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


def validate_length(value, length=16):
    if len(str(value)) != length or not(value.isnumeric()):
        raise ValidationError('NIK Must Contains 16 Digit Number')


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    nama = models.CharField(max_length=255)
    nik = models.CharField(
        validators=[validate_length], max_length=20, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama', 'nik']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    # supaya bisa liat superuser
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
