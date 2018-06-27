from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account.views import IndexView, SettingsView, LoginView, signup, activate
from django.conf import settings
from simple_sso.sso_server.server import Server
sso = Server()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('server/', include(sso.get_urls())),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('login/', auth_views.LoginView.as_view(), {'template_name': 'account/login.html'}, name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(redirect_field_name='next')),
    path('signup/', signup, name='signup'),
]
