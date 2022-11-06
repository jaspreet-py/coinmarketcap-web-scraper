from django.db import models
from django.utils import timezone

# Create your models here.
class Currency(models.Model):
    source = models.CharField(max_length=100, default="")
    updated_on = models.DateTimeField(default=timezone.now)
    data = models.JSONField(default=list)
