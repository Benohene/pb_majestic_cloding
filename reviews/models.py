from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    """
    A review model for maintaining a user's review
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=100, null=True, blank=True)
    review_text = models.TextField(max_length=2000, null=True, blank=True)
    review_date = models.DateTimeField(auto_now_add=True, null=True)
    review_rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    
    
    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ['-review_date']
        
    def __str__(self):
        return f'{self.user.username} - {self.product.name}'