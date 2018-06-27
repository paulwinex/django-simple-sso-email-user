from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.conf import settings
from account.models import EmailUser


class IndexView(TemplateView):
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['site_type'] = 'SERVER' if settings.IS_SSO_SERVER else 'CLIENT'
        return ctx


class SettingsView(TemplateView):
    template_name = 'account/settings.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SettingsView, self).dispatch(request, *args, **kwargs)


class LoginView(TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        ctx = self.get_context_data()
        form = AuthenticationForm(request.POST.dict())
        if not form.is_valid():
            return redirect(request.path)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        check_auth = auth.authenticate(
            email=email,
            password=password
        )
        if not check_auth:
            ctx['form'] = form
            return self.render_to_response(ctx)
        user = get_object_or_404(EmailUser, email=email)
        if not user:
            ctx['form'] = form
            return self.render_to_response(ctx)
        auth.login(request, user)
        return redirect(request.GET.get('next', '/'))

    def get(self, request, **kwargs):
        ctx = self.get_context_data()
        ctx['form'] = AuthenticationForm()
        return self.render_to_response(ctx)
