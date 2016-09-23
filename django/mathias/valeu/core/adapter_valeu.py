from mathias.valeu.models import Valeu


class AdapterValeu():
    def __init__(self, calculate):
        self.calculate = calculate

    def adapter(self):

        users_to = []
        for user in self.calculate.text.split():
            if user[0] == "@":
                users_to.append(user)

        list_valeu = []
        for user in users_to:
            valeu = Valeu.create(self.calculate.team_id, self.calculate.team_domain, self.calculate.channel_id,
                                 self.calculate.channel_name, self.calculate.user_id,
                                 self.calculate.user_name,
                                 "1", user, self.calculate.command, self.calculate.text, self.calculate.response_url)
            list_valeu.append(valeu)

        return list_valeu;
