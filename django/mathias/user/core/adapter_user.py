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
                               (bool(u['status']) if 'status' in u else None),
                               (u['real_name'] if 'real_name' in u else None),
                               (u['profile']['first_name'] if u['profile'] in ['first_name'] else None),
                               (u['profile']['last_name'] if u['profile'] in ['last_name'] else None),
                               (u['profile']['title'] if u['profile'] in ['title'] else None),
                               (u['profile']['email'] if u['profile'] in ['email'] else None),
                               (u['profile']['image_24'] if u['profile'] in ['image_24'] else None),
                               (u['profile']['image_32'] if u['profile'] in ['image_32'] else None),
                               (u['profile']['image_48'] if u['profile'] in ['image_48'] else None),
                               (u['profile']['image_72'] if u['profile'] in ['image_72'] else None),
                               (u['profile']['image_192'] if u['profile'] in ['image_192'] else None),
                               (u['profile']['image_original'] if u['profile'] in ['image_original'] else None))
            list_users.append(user)

        return list_users
