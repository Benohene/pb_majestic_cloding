from django import forms
from products.widgets import CustomClearableFileInput
from .models import Blog, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            'body': SummernoteWidget(),
            'image': CustomClearableFileInput,
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        ''' Intialise form and set focus on title field '''
        self.fields['title'].widget.attrs['autofocus'] = True
        
        ''' Add placeholders and classes to form fields '''
        placeholders = {
            'title': 'Blog Title',
            'body': 'Blog Content',
            'image_url': 'Image URL',
        }
        
        self.fields['title'].widget.attrs['autofocus'] = True
        
        
        for field in self.fields:
            if field != 'image':
                placeholder = f'{placeholders[field]}'
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            
        ''' Remove labels from form fields '''
        for field in self.fields:
            self.fields[field].label = False
            
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        ''' Intialise form and set focus on name field '''
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
            
        ''' Remove labels from form fields '''
        for field in self.fields:
            self.fields[field].label = False
        
