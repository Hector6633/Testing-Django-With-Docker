from django.db import models

# Create your models here.
 
class user(models.Model):
    user_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user_name
    
class Number_user(models.Model):
    phone_no = models.CharField(max_length=10)
    user_id = models.OneToOneField(user, on_delete=models.CASCADE,related_name='number_user')
    
    def __str__(self):
        return self.phone_no
    
class Department(models.Model):
    department_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.department_name
    
class Employee(models.Model):
    employee_name = models.CharField(max_length=10)
    employee_age = models.IntegerField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE,related_name='employee')
    
    def __str__(self):
        return self.employee_name
    
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=10)
    year = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Store(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    books = models.ManyToManyField(Book, related_name='stores')
    def __str__(self):
        return self.name