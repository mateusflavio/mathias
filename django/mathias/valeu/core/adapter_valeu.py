from rest_framework import status

from mathias.user.models import User
from mathias.utils.metadata import MetaError
from mathias.valeu.models import Valeu


class AdapterValeu():
    def __init__(self, valeu):
        self.valeu = valeu

    def adapter(self):

        users_to = []
        for user in self.valeu.text.split():
            if user[0] == "@":
                users_to.append(user)

        count_user_from_in_text = [x for x in users_to if x == '@' + self.valeu.user_name].__len__()

        if count_user_from_in_text > 0:
            meta_error = MetaError('It`s not possible to give /vlw yourself',
                                   'It`s not possible to give /vlw yourself',
                                   status.HTTP_400_BAD_REQUEST)
            return meta_error

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
            meta_error = MetaError('User(s) ' + users_not_exist + ' in /vlw not found',
                                   'User(s) ' + users_not_exist + ' in /vlw not found',
                                   status.HTTP_404_NOT_FOUND)
            return meta_error

        else:
            return list_valeu
