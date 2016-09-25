from django.utils import timezone

from django.db import models

class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    team_id = models.CharField(max_length=50)
    name = models.CharField(max_length=500)
    status = models.BooleanField()
    real_name = models.CharField(max_length=500)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    title = models.CharField(max_length=700)
    email = models.CharField(max_length=200)
    image_24 = models.CharField(max_length=300)
    image_32 = models.CharField(max_length=300)
    image_48 = models.CharField(max_length=300)
    image_72 = models.CharField(max_length=300)
    image_192 = models.CharField(max_length=300)
    image_original = models.CharField(max_length=300)
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'user'

    def save(self, *args, **kwargs):
        self.create_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    @classmethod
    def create(cls, id, team_id, name, status, real_name, first_name, last_name, title, email,
               image_24, image_32, image_48, image_72, image_192, image_original):
        user = cls(id=id, team_id=team_id, name=name, status=status, real_name=real_name, first_name=first_name,
                   last_name=last_name, title=title, email=email, image_24=image_24, image_32=image_32,
                   image_48=image_48, image_72=image_72, image_192=image_192, image_original=image_original)
        return user

#
# "id": "U04KHGD7V",
# "team_id": "T024FR42U",
# "name": "aldren.moraes",
# "deleted": false,
# "status": null,
# "color": "3c989f",
# "real_name": "Aldren Moraes",
# "tz": "America/Sao_Paulo",
# "tz_label": "Brasilia Time",
# "tz_offset": -10800,
# "profile": {
#     "first_name": "Aldren",
#     "last_name": "Moraes",
#     "title": "Coordenador Infraestrutura",
#     "skype": "aldren.moraes",
#     "phone": "11993293679",
#     "image_24": "https://avatars.slack-edge.com/2016-09-14/79789507841_316c4bb3db97b4b8720b_24.png",
#     "image_32": "https://avatars.slack-edge.com/2016-09-14/79789507841_316c4bb3db97b4b8720b_32.png",
#     "image_48": "https://avatars.slack-edge.com/2016-09-14/79789507841_316c4bb3db97b4b8720b_48.png",
#     "image_72": "https://avatars.slack-edge.com/2016-09-14/79789507841_316c4bb3db97b4b8720b_72.png",
#     "image_192": "https://avatars.slack-edge.com/2016-09-14/79789507841_316c4bb3db97b4b8720b_192.png",
#     "image_original": "https://avatars.slack-edge.com/2016-09-14/79789507841_316c4bb3db97b4b8720b_original.png",
#     "avatar_hash": "316c4bb3db97",
#     "image_512": "https://avatars.slack-edge.com/2016-09-14/79789507841_316c4bb3db97b4b8720b_512.png",
#     "image_1024": "https://avatars.slack-edge.com/2016-09-14/79789507841_316c4bb3db97b4b8720b_512.png",
#     "real_name": "Aldren Moraes",
#     "real_name_normalized": "Aldren Moraes",
#     "email": "aldren.moraes@luizalabs.com"