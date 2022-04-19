from django.db import models



# Create your models here
from user.models import Location


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    qty_stock = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    category_name = models.ForeignKey('Category', related_name='Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    company_name = models.CharField(max_length=100)
    location_id = models.OneToOneField(Location, related_name='Location', on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=100)
    product= models.ManyToManyField(Product)

    def __str__(self):
        return self.company_name

