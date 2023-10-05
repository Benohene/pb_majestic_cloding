'''Admin for profiles app'''
from django.contrib import admin
from .models import UserProfile, Wishlist

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    '''Admin for user profiles'''
    list_display = (
        "user",
        "default_full_name",
        "default_phone_number",
        "default_street_address1",
        "default_street_address2",
        "default_town_or_city",
        "default_region",
        "default_postcode",
        "default_country",
    )

    search_fields = (
        "user",
        "default_full_name",
    )

    ordering = ("user",)


class WishlistAdmin(admin.ModelAdmin):
    '''Admin for wishlists'''
    list_display = ("user",)

    search_fields = ("user",)

    ordering = ("user",)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Wishlist, WishlistAdmin)
