''' This file contains the models for the products app. '''
from django.db import models


# Create your models here.
class Category(models.Model):
    ''' This class will create the category model '''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        ''' This will change the name of the model in the admin panel '''
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        ''' This will return the name of the category '''
        return self.name

    def get_friendly_name(self):
        ''' This will return the friendly name of the category '''
        return self.friendly_name


class Product(models.Model):
    ''' This class will create the product model '''
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
