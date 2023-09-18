from django.db import models

# Create your models here.
#model for department
class Department(models.Model):
    Department_Name = models.CharField(max_length=100,null=True)
    
    class Meta:
        verbose_name_plural = 'Department'
    
    def __str__(self):
        return f'{self.Department_Name}'
    
#model for division 
class Division(models.Model):
    Division_Name = models.CharField(max_length=100,null=True)
    Department_Name = models.CharField(max_length=100,null=True)
    
    class Meta:
        verbose_name_plural = 'Division'
    
    def __str__(self):
        return f'{self.Division_Name}-{self.Department_Name}'

#model for unit
class Unit(models.Model):
    Unit_Name = models.CharField(max_length=100,null=True)
    Department_Name = models.CharField(max_length=100,null=True)
    
    class Meta:
        verbose_name_plural = 'Unit'
    
    def __str__(self):
        return f'{self.Unit_Name}-{self.Department_Name}'

#model for staff
class Staff(models.Model):
    Staff_Id = models.CharField(max_length=100,null=True)
    Staff_Name = models.CharField(max_length=100,null=True)
    Department_Name = models.CharField(max_length=100,null=True)
    Division_Name = models.CharField(max_length=100,null=True)
    Unit_Name = models.CharField(max_length=100,null=True)
    Section_Name = models.CharField(max_length=100,null=True,default='No Section')
    Date_First_app = models.DateField(max_length=100,null=True)
    Date_Present_app = models.DateField(max_length=100,null=True)
    Cadre = models.CharField(max_length=100,null=True)
    Rank_position = models.CharField(max_length=100,null=True)
    Gloconraiss = models.CharField(max_length=100,null=True)
    DOB = models.DateField(max_length=100,null=True)
    File_No = models.CharField(max_length=100,null=True)
    Geo_Political_zone = models.CharField(max_length=100,null=True)
    State = models.CharField(max_length=100,null=True)
    Local_Gov_Area = models.CharField(max_length=100,null=True)
    IPPS = models.CharField(max_length=100,null=True)
    
    class Meta:
        verbose_name_plural = 'Staff List'
    
    def __str__(self):
        return f'{self.Staff_Id}-{self.Staff_Name}-{self.DOB}-{self.Cadre}-{self.File_No}'
