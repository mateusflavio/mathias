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
        for user in users_to:
            valeu = Valeu.create(self.valeu.team_id, self.valeu.team_domain, self.valeu.channel_id,
                                 self.valeu.channel_name, self.valeu.user_id,
                                 self.valeu.user_name,
                                 "1", user, self.valeu.command, self.valeu.text, self.valeu.response_url)
            list_valeu.append(valeu)

        return list_valeu;
