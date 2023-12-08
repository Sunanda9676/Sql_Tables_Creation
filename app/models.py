from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(self):
        return self.dname

class Emp(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename

class Salgrade(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    deptno=models.IntegerField()
    salgrade=models.ForeignKey(Emp,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename

class Bonus(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    bonus=models.ForeignKey(Salgrade,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename    