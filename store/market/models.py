from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    # 1. Soda


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    price = models.FloatField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    best_before_date = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=7))

    def __str__(self):
        return self.name

    # category_id = 1

class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
