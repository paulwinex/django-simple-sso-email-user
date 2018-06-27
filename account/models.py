from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# from .managers import CustomUserManager
#
#
# class EmailUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, null=True)
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this admin site.'),
#     )
#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#
#     def get_full_name(self):
#         return self.email
#
#     def get_short_name(self):
#         return self.get_full_name()
#
#     def __str__(self):
#         return self.email
#


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    lang = models.CharField(_('Language'), max_length=4, default='en', choices=settings.LANGUAGES)
    url = models.URLField(_('URL'), null=True, blank=True)

    def __str__(self):
        return 'User Profile {}'.format(self.user)

    def __repr__(self):
        return 'User Profile {}'.format(self.user)
