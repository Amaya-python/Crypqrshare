from django.db import models


class Vcmsg(models.Model):
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'vcmsg'

