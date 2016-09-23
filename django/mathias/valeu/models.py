from django.db import models
from django.utils import timezone

class Valeu(models.Model):
    id = models.AutoField(primary_key=True)
    team_id = models.IntegerField()
    team_domain = models.CharField(max_length=500)
    channel_id = models.CharField(max_length=50)
    channel_name = models.CharField(max_length=500)
    user_id_from = models.CharField(max_length=80)
    user_name_from = models.CharField(max_length=500)
    user_id_to = models.CharField(max_length=80)
    user_name_to = models.CharField(max_length=500)
    command = models.CharField(max_length=100)
    text = models.CharField(max_length=800)
    response_url = models.CharField(max_length=600)
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'valeu'

    @classmethod
    def create(cls, team_id, team_domain, channel_id, channel_name, user_id_from, user_name_from,
               user_id_to, user_name_to, command, text, response_url):
        valeu = cls(team_id=team_id, team_domain=team_domain, channel_id=channel_id, channel_name=channel_name,
                    user_id_from=user_id_from, user_name_from=user_name_from, user_id_to=user_id_to,
                    user_name_to=user_name_to, command=command, text=text, response_url=response_url)
        return valeu

    def save(self, *args, **kwargs):
        self.create_at = timezone.now()
        return super(Valeu, self).save(*args, **kwargs)


class SaveValeu(object):
    def __init__(self, token, team_id, team_domain, channel_id, channel_name, user_id, user_name, command, text,
                 response_url):
        self.token = token
        self.team_id = team_id
        self.team_domain = team_domain
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.user_id = user_id
        self.user_name = user_name
        self.command = command
        self.text = text
        self.response_url = response_url
