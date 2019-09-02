from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # This field determines if the user is admin
    #is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'password']
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username
