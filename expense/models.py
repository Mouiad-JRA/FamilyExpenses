from django.db import models
from django.utils.timezone import now

from accounts.models import User


class Material(models.Model):
    name = models.CharField(max_length=255)
    is_service = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return f"This Material name is {self.name}"


class OutlayType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Outlay(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    outlay_type = models.ForeignKey(OutlayType, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=3)
    date = models.DateField(default=now())
    description = models.TextField()

    def __str__(self):
        return f"This Expense for{self.description} which belong to {self.owner.username} with amount {self.price}"

    class Meta:
        ordering: ['-data']
