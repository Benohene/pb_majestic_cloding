from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    # forms to add/edit/delete reviews
    class Meta:
        model = Review
        fields = ("review_title", "review_text", "review_rating")

        labels = {
            "review_title": "Review Title",
            "review_text": "Review Text",
            "review_rating": "Review Rating (1-5)",
        }

        # override the init method to add placeholders and classes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "review_title": "Review Title",
            "review_text": "Review Text",
            "review_rating": "Review Rating (1-5)",
        }

        # set autofocus on first field
        self.fields["review_title"].widget.attrs["autofocus"] = True

        # set review rating field to number input type
        self.fields["review_rating"].widget.attrs["type"] = "number"
        self.fields["review_rating"].widget.attrs["min"] = "1"
        self.fields["review_rating"].widget.attrs["max"] = "5"
