from django.db import models

class Employee(models.Model):
    Id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(default=0)
    salary=models.IntegerField(default=3000)
    dsg=models.CharField(max_length=20)
    city=models.CharField(max_length=20,blank=True,null=True,default="Noida")
    state=models.CharField(max_length=20,blank=True,null=True,default="UP")

    def __str__(self):
        return str(self.Id)+" "+self.name+" "+self.email

