from django.db import models
from gut_matrices.models import GutMatrix

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
    requester_email = models.EmailField(blank=False, null=False)
    origin = models.TextField(blank=False, null=False, max_length=5000)
    status = models.CharField(choices=STATUS, null=False, max_length=20, default='ABERTA')
    gut_matrix = models.ForeignKey(GutMatrix, related_name='gut_matrix', on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-gut_matrix__gut' ,'-created_at']