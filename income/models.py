from django.db import models
from django.utils.timezone import now
from accounts.models import User


class Source(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=3, null=False)
    date = models.DateField(default=now())
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return f"This income for{self.description} which belong to {self.owner.username}"

    class Meta:
        ordering: ['-date']
