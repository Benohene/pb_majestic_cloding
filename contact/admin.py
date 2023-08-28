"""This file is used to register the models in the admin panel."""
from django.contrib import admin
from .models import ContactMail


class ContactMailAdmin(admin.ModelAdmin):
    """Admin model for contact app."""

    list_display = (
        "full_name",
        "email",
        "subject",
        "enquiry_type",
        "date_sent",
        "replied",
    )

    list_filter = ("enquiry_type", "replied")
    ordering = ("-date_sent",)


admin.site.register(ContactMail, ContactMailAdmin)
