from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, ImageField, TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for PAPE.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    address = CharField(_("Address"), max_length=255, blank=True)
    phone_number = CharField(_("Phone Number"), max_length=15, blank=True)

    # Agrega un campo para el tipo de usuario (propietario o paseador)
    # Puedes usar un campo de elección (ChoiceField) o un campo booleano
    USER_TYPE_CHOICES = (
        ("owner", "Propietario"),
        ("walker", "Paseador"),
    )
    user_type = CharField(_("User Type"), max_length=10, choices=USER_TYPE_CHOICES, default="owner")
    password_reset_token = CharField(_("Password Reset Token"), max_length=100, blank=True)
    password_reset_expires = DateTimeField(_("Password Reset Token Expiration"), null=True, blank=True)

    # Campos relacionados con perfiles de usuario
    bio = TextField(_("Bio"), blank=True)
    profile_picture = ImageField(_("Profile Picture"), upload_to="profile_pictures/", blank=True)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.username
