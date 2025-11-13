from django.db import models
from work.models import Work
from manager_reg.models import ManagerReg

# Create your models here.
class AssignWorkManager(models.Model):
    assign_id = models.AutoField(primary_key=True)
    # work_id = models.IntegerField()
    work = models.ForeignKey(Work,on_delete=models.CASCADE)
    work_details = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    work_status = models.CharField(max_length=45)
    # manager_id = models.IntegerField()
    manager = models.ForeignKey(ManagerReg,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'assign_work_manager'

