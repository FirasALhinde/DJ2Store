from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/')
    category =models.ForeignKey('Category',related_name='product_category',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return  self.name