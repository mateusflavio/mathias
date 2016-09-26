from mathias.user.models import User


class AdapterUser:
    def __init__(self, users):
        self.users = users

    def adapter(self):
        list_users = []
        for u in self.users:

            user = User.create(u['id'],
                               (u['team_id'] if 'team_id' in u else None),
                               (u['name'] if 'name' in u else None),
                               (bool(u['status']) if 'status' in u else False),
                               (u['real_name'] if 'real_name' in u else None),
                               (u['profile']['first_name'] if 'first_name' in u['profile'] else None),
                               (u['profile']['last_name'] if 'last_name' in u['profile'] else None),
                               (u['profile']['title'] if 'title' in u['profile'] else None),
                               (u['profile']['email'] if 'email' in u['profile'] else None),
                               (u['profile']['image_24'] if 'image_24' in u['profile'] else None),
                               (u['profile']['image_32'] if 'image_32' in u['profile'] else None),
                               (u['profile']['image_48'] if 'image_48' in u['profile'] else None),
                               (u['profile']['image_72'] if 'image_72' in u['profile'] else None),
                               (u['profile']['image_192'] if 'image_192' in u['profile'] else None),
                               (u['profile']['image_original'] if 'image_original' in u['profile'] else None))
            list_users.append(user)

        return list_users
