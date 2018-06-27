from simple_sso.sso_server.models import Token, Consumer
from django.conf import settings


# for server
if not Consumer.objects.all().count():
    print('Create SSO Consumer')
    Consumer.objects.create(
        public_key=settings.DEFAULT_SSO_PUBLIC_KEY,
        private_key=settings.DEFAULT_SSO_PRIVATE_KEY,
        name='default'
    )
else:
    print('Skip  SSO Consumer creation')
