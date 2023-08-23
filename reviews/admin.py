from django.contrib import admin
from .models import Review

# Register your models here.
'''
The ReviewAdmin class is used to customise the admin interface to display the
fields we want and in the order we want
'''

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_title',
        'user',
        'product',
        'review_date',
        'review_rating',
    )
    
    ordering = ('review_date',)
    
    search_fields = (
        'user',
        'product',
    )
    
    list_filter	= (
        'review_date',
        'review_rating',
    )
    
admin.site.register(Review, ReviewAdmin)