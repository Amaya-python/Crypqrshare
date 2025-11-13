from django.db import models
from manager_reg.models import ManagerReg
from employee_reg.models import EmployeeReg
from assign_work_manager.models import AssignWorkManager

# Create your models here.
class AssignWorkEmployee(models.Model):
    assign_emp_id = models.AutoField(primary_key=True)
    # assign_id = models.IntegerField()
    assign=models.ForeignKey(AssignWorkManager, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    work_status = models.CharField(max_length=45)
    # manager_id = models.IntegerField()
    manager = models.ForeignKey(ManagerReg,on_delete=models.CASCADE)
    # emp_id = models.IntegerField()
    emp = models.ForeignKey(EmployeeReg,on_delete=models.CASCADE)
    description = models.CharField(max_length=450)

    class Meta:
        managed = False
        db_table = 'assign_work_employee'

