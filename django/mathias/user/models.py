from django.utils import timezone

from django.db import models


class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    team_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    real_name = models.CharField(max_length=500, null=True)
    first_name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=700, null=True)
    email = models.CharField(max_length=200, null=True)
    image_24 = models.CharField(max_length=300, null=True)
    image_32 = models.CharField(max_length=300, null=True)
    image_48 = models.CharField(max_length=300, null=True)
    image_72 = models.CharField(max_length=300, null=True)
    image_192 = models.CharField(max_length=300, null=True)
    image_original = models.CharField(max_length=300, null=True)
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
