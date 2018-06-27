# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from account.models import EmailUser
# # from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _
#
#
# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')
#
#     class Meta:
#         model = EmailUser
#         fields = ('email', 'password1', 'password2')
#
#
# class LoginForm(forms.Form):
#
#     email = forms.EmailField(
#         max_length=254,
#         widget=forms.TextInput(attrs={'autofocus': True}),
#         label=_("Email")
#     )
#     password = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput,
#     )
#
#
# class RestForm(forms.Form):
#     email = forms.EmailField(
#         max_length=254,
#         widget=forms.TextInput(attrs={'autofocus': True}),
#         label=_("Email")
#     )
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         check = EmailUser.objects.filter(email=email)
#         if not check:
#             raise forms.ValidationError(_('No email'))
#
#         return email
#
#
# class ChangePasswordForm(forms.Form):
#
#     password_1 = forms.PasswordInput()
#     password_2 = forms.PasswordInput()
#
#     def clean(self):
#         password_1 = self.cleaned_data['password_1']
#         password_2 = self.cleaned_data['password_2']
#
#         if password_1 != password_2:
#             raise forms.ValidationError(_('Password 1 '))
