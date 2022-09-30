from django.db import models

# Create your models here.
from accounts.forms import User


class UserPerference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{str(self.user.username)} s perferences"