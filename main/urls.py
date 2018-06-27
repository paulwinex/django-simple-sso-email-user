from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account.views import IndexView, SettingsView
from django.conf import settings

from sso_email_user.server import Server
sso_server = Server()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('login/', auth_views.LoginView.as_view(), {'template_name': 'account/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(redirect_field_name='next')),
]
if settings.IS_SSO_SERVER:
    urlpatterns.insert(3, path('server/', include(sso_server.get_urls())))
else:
    from sso_email_user.client import Client
    sso_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)
    sso_client.user_extra_data = ['lang']
    urlpatterns.insert(3, path('client/', include(sso_client.get_urls())))
