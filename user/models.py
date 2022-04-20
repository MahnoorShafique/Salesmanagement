from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Location(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=50)

    def __str__(self):
        return self.province


class Job(models.Model):
    job_title = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    def __str__(self):
        return self.job_title


class Type(models.Model):
    type = models.CharField(max_length=100)


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type_id = models.CharField(max_length=100)
    location_id = models.OneToOneField(Location, on_delete=models.CASCADE, null=True, blank=True, default=None)
    phone_num = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user_name


class Manager(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_num = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField()
    location_id = models.OneToOneField(Location, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.first_name


class Employee(User):
    job_id = models.OneToOneField(Job, on_delete=models.CASCADE, null=True, blank=True, default=None)
    hire_date = models.DateField(default=None)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.user_name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_num = models.PositiveIntegerField(null=True, blank=True)
    employee = models.ManyToManyField(Employee)

    def __str__(self):
        return self.first_name
