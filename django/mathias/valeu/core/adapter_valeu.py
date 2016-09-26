from mathias.user.models import User
from mathias.valeu.models import Valeu


class AdapterValeu():
    def __init__(self, valeu):
        self.valeu = valeu

    def adapter(self):

        users_to = []
        for user in self.valeu.text.split():
            if user[0] == "@":
                users_to.append(user)

        list_valeu = []
        users_not_exist = ''
        for user in users_to:

            user_string = '''''' + user.replace('@', '') + ''''''

            try:

                user_object = User.objects.get(name=user_string)

                if user_object:

                    text_string = self.valeu.text.replace(user, '<@' + user_object.id + '>')

                    valeu = Valeu.create(self.valeu.team_id, self.valeu.team_domain, self.valeu.channel_id,
                                         self.valeu.channel_name, self.valeu.user_id,
                                         self.valeu.user_name,
                                         user_object.id, user.replace('@', ''), self.valeu.command, text_string,
                                         self.valeu.response_url)
                    list_valeu.append(valeu)

                else:
                    users_not_exist = users_not_exist + user + ' '

            except Exception as e:
                users_not_exist = users_not_exist + user + ' '

        if users_not_exist:
            return users_not_exist
        else:
            return list_valeu
