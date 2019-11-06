from django.db import models

class Demand(models.Model):
    # Dict que define os possíveis status da demanda
    STATUS = (
        ('ABERTA', 'ABERTA'),
        ('EM ANDAMENTO', 'EM ANDAMENTO'),
        ('FECHADA', 'FECHADA'),
    )

    name = models.CharField(blank=False, null=False, max_length=100, unique=True)
    description = models.TextField(blank=False, null=False, max_length=5000)
    requester = models.CharField(blank=False, null=False, max_length=70)
    origin = models.TextField(blank=False, null=False, max_length=5000)
    status = models.CharField(choices=STATUS, null=False, max_length=20, default='ABERTA')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']