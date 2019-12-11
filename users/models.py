from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_project_manager', True)
        extra_fields.setdefault('is_demand_manager', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        if extra_fields.get('is_project_manager') is not True:
            raise ValueError('Superuser must have is_project_manager=True.')
        if extra_fields.get('is_demand_manager') is not True:
            raise ValueError('Superuser must have is_demand_manager=True.')

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    # This field determines if the user is admin
    is_admin = models.BooleanField(default=False)
    # This field determines if user can manager opening terms
    is_project_manager = models.BooleanField(default=False)
    # This field determines if user can manager demands
    is_demand_manager = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'password']

    objects = UserManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username
