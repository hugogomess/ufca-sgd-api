from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # This field determines if the user is admin
    is_admin = models.BooleanField(
        'admin status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['first_name', 'email']

    def __str__(self):
        return self.username
