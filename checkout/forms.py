from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    # This class is used to create the order form
    model = Order
    fields = ('full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'region',)
    
    
    # Code taken from Code Institute Boutique Ado project
    def __init__(self, *args, **kwargs):
        # Add placeholders and classes to form inputs
        # Code taken from Code Institute Boutique Ado project
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'region': 'Region',
        }
        
        # Code taken from Code Institute Boutique Ado project
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Code taken from Code Institute Boutique Ado project
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                    
                # Code taken from Code Institute Boutique Ado project
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False