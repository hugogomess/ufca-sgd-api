from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class GutMatrix(models.Model):

    name = models.CharField(blank=False, null=False, max_length=2000)
    gravity = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1),MaxValueValidator(5)])
    urgency = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1),MaxValueValidator(5)])
    trend = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1),MaxValueValidator(5)])
    gut = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1),MaxValueValidator(125)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']