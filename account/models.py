from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
# from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import django
# FOR EMAIL USER
from django.utils import timezone
from .managers import CustomUserManager, EmailUserManager


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):

    """
    Abstract User with the same behaviour as Django's default User.
    AbstractEmailUser does not have username field. Uses email as the
    USERNAME_FIELD for authentication.
    Use this if you need to extend EmailUser.
    Inherits from both the AbstractBaseUser and PermissionMixin.
    The following attributes are inherited from the superclasses:
        * password
        * last_login
        * is_superuser
    """

    email = models.EmailField(_('email address'), max_length=255,
                              unique=True, db_index=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = EmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:  # noqa: D101
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """Return the email."""
        return self.email

    def get_short_name(self):
        """Return the email."""
        return self.email

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this User."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)


# Monkey patch Django 1.7 to avoid detecting migrations
if django.VERSION[:2] == (1, 7):
    last_login = AbstractEmailUser._meta.get_field('last_login')
    last_login.blank = True
    last_login.null = True
    last_login.default = models.fields.NOT_PROVIDED
    groups = AbstractEmailUser._meta.get_field('groups')
    groups.help_text = _('The groups this user belongs to. A user will get '
                         'all permissions granted to each of their groups.')


class EmailUser(AbstractEmailUser):

    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    class Meta(AbstractEmailUser.Meta):  # noqa: D101
        swappable = 'AUTH_USER_MODEL'

    @property
    def lang(self):
        try:
            return Profile.objects.get(user=self).lang
        except Profile.DoesNotExist:
            print('DEFAULT LANG')
            return 'en'


class Profile(models.Model):
    user = models.OneToOneField(EmailUser, on_delete=models.CASCADE, null=False)
    lang = models.CharField(_('Language'), max_length=4, default='en', choices=settings.LANGUAGES)
    url = models.URLField(_('URL'), null=True, blank=True)

    def __str__(self):
        return 'User Profile {}'.format(self.user)

    def __repr__(self):
        return 'User Profile {}'.format(self.user)
