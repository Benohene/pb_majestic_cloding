"""Email model for contact app."""
from django.db import models


ENQUIRY_TYPE = (
    ("General Enquiry", "General Enquiry"),
    ("Customer Service", "Customer Service"),
    ("Product Support", "Product Support"),
    ("Other", "Other"),
)


class ContactMail(models.Model):
    """Email model for contact app."""

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    enquiry_type = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=ENQUIRY_TYPE,
        default="General Enquiry",
    )
    subject = models.CharField(
        max_length=254, null=False, blank=False, default=""
    )
    message = models.TextField(null=False, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.full_name}"
