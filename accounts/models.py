from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Family(models.Model):
    """ Family Model """
    family_name = models.CharField(_("Name of Family Name"), blank=True, max_length=255)


class User(AbstractUser):
    """ Custom User Model """

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='users')
    picture = models.ImageField(_("Picture"), null=True, blank=True)
    head = models.OneToOneField(Family, on_delete=models.CASCADE, related_name='familyhead')

    def __str__(self):
        return self.get_full_name()

    def set_picture(self, picture_data):
        try:
            if picture_data is not None and all(
                    [picture_data.get("path", False), picture_data.get("filename", False)]
            ):
                with open(picture_data["path"], "rb") as f:
                    self.picture.save(picture_data["filename"], f)
        except FileNotFoundError:
            pass
