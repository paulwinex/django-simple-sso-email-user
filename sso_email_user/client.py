from simple_sso.sso_client.client import Client as DefaultClient
from django.contrib.auth import get_user_model
User = get_user_model()


class Client(DefaultClient):
    def build_user(self, user_data):
        try:
            user = User.objects.get(email=user_data['email'])
        except User.DoesNotExist:
            user = User(**user_data)
        user.set_unusable_password()
        user.save()
        return user
