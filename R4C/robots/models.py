from django.db import models

from orders.models import Order


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False, unique=True)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.model} {self.version} - {self.created}"
