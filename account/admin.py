from django.contrib import admin
from .models import EmailUser
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from .forms import EmailUserChangeForm, EmailUserCreationForm
from django.utils.translation import ugettext_lazy as _


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':
                ('user',
                 'url',
                 'lang',
                )
                },),
    )
    ordering = []
    list_display = ('user',)


# FOR EMAIL USER
# @admin.register(EmailUser)
# class EmailUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {
#             'fields':
#                 ('email', 'password',
#                  'is_superuser',
#                  'is_staff',
#                  'is_active',
#                  'last_login')
#                 },),
#     )
#     ordering = []
#     readonly_fields = ('last_login', )
#     list_display = ('email', 'last_login')

@admin.register(EmailUser)
class EmailUserAdmin(UserAdmin):

    """EmailUser Admin model."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }
    ),
    )

    # The forms to add and change user instances
    form = EmailUserChangeForm
    add_form = EmailUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
