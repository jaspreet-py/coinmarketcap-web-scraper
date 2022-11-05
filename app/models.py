from django.db import models

# Create your models here.
class Currency(models.Model):
    class Meta:
        ordering: list[str] = ["-mcap"]

    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    price = models.FloatField()
    change = models.JSONField()
    mcap = models.BigIntegerField()
    volume = models.JSONField()
    c_supply = models.BigIntegerField()
