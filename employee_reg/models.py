from django.db import models
from manager_reg.models import ManagerReg

# Create your models here.
class EmployeeReg(models.Model):
    emp_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    pincode = models.IntegerField()
    phone_number = models.CharField(max_length=45)
    marital_status = models.CharField(max_length=45)
    join_date = models.DateField()
    type = models.CharField(max_length=45)
    # manager_id = models.CharField(max_length=45)
    manager = models.ForeignKey(ManagerReg,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    username = models.CharField(max_length=45)



    class Meta:
        managed = False
        db_table = 'employee_reg'
