from distutils.command.upload import upload
import black
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models 

class User(AbstractUser):
    """
    Default custom user model for Final.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("First Name"), blank=True, max_length=255)  # type: ignore
    last_name = CharField(_("Last Name"), blank=True, max_length=255)  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Avatar(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars', null=True, blank= True)