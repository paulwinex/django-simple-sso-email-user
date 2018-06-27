from django.contrib import admin
# from .models import EmailUser
from .models import Profile
# from django.contrib.auth.admin import UserAdmin


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