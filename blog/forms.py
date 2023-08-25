''' Blog form for admin to add/edit blog posts '''
from django_summernote.widgets import SummernoteWidget
from django import forms
from products.widgets import CustomClearableFileInput
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    """
    Form to Create/Edit Blog
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = Blog
        fields = "__all__"
        exclude = [
            "created_on",
            "likes",
            "author",
        ]

        widgets = {
            "body": SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
            "image": CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initializes the form attributes
        """
        placeholders = {
            "title": "Enter Blog Title",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(
                field_name, ""
            )
        self.fields["title"].widget.attrs["autofocus"] = True


class CommentForm(forms.ModelForm):
    ''' Form to add comments to blog posts '''

    class Meta:
        ''' Meta class to define model and fields to be used in form '''
        model = Comment
        fields = ('name', 'body')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['autofocus'] = True

        ''' Add placeholders and classes to form fields '''
        placeholders = {
            'name': 'Name',
            'body': 'Comment',
        }

        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'

        for field in self.fields:
            self.fields[field].label = False
