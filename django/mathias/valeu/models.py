from django.db import models
from django.utils import timezone

class Valeu(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    message = models.CharField(max_length=400)
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'valeu'

    def save(self, *args, **kwargs):
        self.create_at = timezone.now()
        return super(Valeu, self).save(*args, **kwargs)


