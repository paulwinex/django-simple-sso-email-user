# from account.models import EmailUser as User
from django.contrib.auth.models import User

username = 'admin'
# email = 'admin@gmail.com',
password = '123'


# if not User.objects.filter(email=email).exists():
if not User.objects.filter(username=username).exists():
    print('Create Super User\n {}:{}'.format(username, password))
    u = User.objects.create(username=username)
    u.is_staff = True
    u.is_superuser = True
    u.is_active = True
    u.set_password(password)
    u.save()
else:
    print('User already exists\n {}:{}'.format(username, password))
