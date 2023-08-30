"""Forms for contact app"""
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ContactMail


class ContactMailForm(forms.ModelForm):
    """Form for contact app."""

    class Meta:
        """Meta class for contact app"""

        model = ContactMail
        fields = (
            "full_name",
            "email",
            "enquiry_type",
            "subject",
            "message",
        )
        widgets = {
            "message": SummernoteWidget(
                attrs={
                    "summernote": {"width": "100%", "height": "400px"}
                }
            ),
        }

        labels = {
            "full_name": "Full Name",
            "email": "Email Address",
            "enquiry_type": "Enquiry Type",
            "subject": "Subject",
            "message": "Message",
        }

    def __init__(self, *args, **kwargs):
        """Init method for contact app"""
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Enter Full Name",
            "email": "Enter Email Address",
            "subject": "Enter Message Subject",
            "message": "Enter Message",
        }
        exclude_fields = ["enquiry_type"]

        for field_name, field in self.fields.items():
            if field_name not in exclude_fields:
                field.widget.attrs["placeholder"] = placeholders.get(
                    field_name, ""
                )
        self.fields["full_name"].widget.attrs["autofocus"] = True
