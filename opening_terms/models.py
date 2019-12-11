from django.db import models
from demands.models import Demand

class OpeningTerm(models.Model):

    project_name = models.CharField(blank=False, null=False, max_length=250)
    demand = models.ForeignKey(Demand, related_name='demand', on_delete=models.DO_NOTHING, blank=False, null=False)
    # Arquivo do termo de abertura
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']