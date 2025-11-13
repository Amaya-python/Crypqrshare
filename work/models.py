from django.db import models

# Create your models here.
class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    file = models.CharField(max_length=100)
    date = models.DateField()
    work_status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'work'
