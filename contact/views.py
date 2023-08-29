"""A view to return the contact page"""
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.conf import settings
from .forms import ContactMailForm


def contact(request):
    """A view to return the contact page"""
    if request.method == "POST":
        form = ContactMailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["full_name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = "Thanks for getting in touch with PB Majestic Cloding!"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [email]

            html_message = render_to_string(
                "contact/emails/email_confirmation.html",
                {"name": name, "message": message, "email": email},
            )
            plain_message = strip_tags(html_message)
            messages.success(
                request,
                f"Thanks {name}, we have received your message and will be in touch soon on {email}.",
            )

            send_mail(
                subject, plain_message, from_email, to_email, html_message=html_message
            )
            return redirect("contact")
        else:
            messages.error(
                request,
                "Your message could not be sent. \
                Please ensure the form is valid.",
            )
    else:
        form = ContactMailForm()

    template = "contact/contact.html"
    context = {
        "form": form,
        "on_contact_page": True,
    }
    return render(request, template, context)
