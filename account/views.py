from django.views.generic import TemplateView
# from .forms import SignupForm, LoginForm, RestForm, ChangePasswordForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .tokens import account_activation_token
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
from account.models import EmailUser
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string


class IndexView(TemplateView):
    template_name = 'account/index.html'


class SettingsView(TemplateView):
    template_name = 'account/settings.html'


class LoginView(TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        print(request.POST.dict())
        ctx = self.get_context_data()
        form = AuthenticationForm(request.POST.dict())
        if not form.is_valid():
            print('not valid', form.error_messages)
            return redirect(request.path)
        # username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        check_auth = authenticate(
            email=email,
            password=password
        )
        if not check_auth:
            ctx['form'] = form
            return self.render_to_response(ctx)
        # user = get_object_or_404(User, username=username)
        user = get_object_or_404(EmailUser, email=email)
        if not user:
            ctx['form'] = form
            return self.render_to_response(ctx)
        auth.login(request, user)
        return redirect(request.GET.get('next', '/'))
    # else:
    #     return render(request, 'account/login.html', {'form': LoginForm()})

    def get(self, request, **kwargs):
        ctx = self.get_context_data()
        ctx['form'] = AuthenticationForm()
        return self.render_to_response(ctx)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('account/acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
                'token': account_activation_token.make_token(user),
            })

            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = _('Activate your account.')
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse(_('Please confirm your email address to complete the registration.'))
            # return render(request, 'acc_active_sent.html')
    else:
        form = UserCreationForm()

    return render(request, 'account/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse(_('Thank you for your email confirmation. Now you can login your account.'))
    else:
        return HttpResponse(_('Activation link is invalid!'))