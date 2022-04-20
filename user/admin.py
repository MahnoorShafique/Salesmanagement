from django.contrib import admin

# Register your models here.
from user.models import Manager, Employee, Customer, Job, Location

admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(Location)