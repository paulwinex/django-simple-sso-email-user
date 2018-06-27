from simple_sso.sso_server.server import Server as DefauleServer


class Server(DefauleServer):
    def get_user_data(self, user, consumer, extra_data=None):
        user_data = {
            'email': user.email,
            'is_staff': False,
            'is_superuser': False,
            'is_active': user.is_active,
        }
        if extra_data:
            user_data['extra_data'] = self.get_user_extra_data(
                user, consumer, extra_data)
        else:
            user_data['extra_data'] = {1:2, 3:4}
        return user_data

    def get_user_extra_data(self, user, consumer, extra_data):
        data = {}
        for name in extra_data:
            try:
                data[name] = getattr(user, name)
            except AttributeError:
                print('Error extra attribute not exists: {}'.format(name))
                continue
        return data