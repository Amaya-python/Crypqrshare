from django.db import models
from employee_reg.models import EmployeeReg


# Create your models here.
class Feedback(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=45)
    reply = models.CharField(max_length=45)
    # emp_id = models.IntegerField()
    emp = models.ForeignKey(EmployeeReg,on_delete=models.CASCADE)
    comp_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'feedback'

