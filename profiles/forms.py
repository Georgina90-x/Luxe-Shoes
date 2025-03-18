from django import forms
from .models import UserProfile
from django_countries.widgets import CountrySelectWidget


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Adds placeholders and classes, removes auto-generated
        labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town/City',
            'default_county': 'County or State',
            'default_postcode': 'Postal Code',
            'default_country': 'Country',  # remove if country fields works
            'default_phone_number': 'Phone Number',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-black rounded profile-form-input'
                self.fields[field].label = False

                # PUT THIS CODE BACK IN IF COUNTRY FIELDS WORKS
            #if field != 'default_country':
                #if self.fields[field].required:
                    #placeholder = f'{placeholders[field]} *'
                #else:
                    #placeholder = placeholders[field]
                #self.fields[field].widget.attrs['placeholder'] = placeholder
                #self.fields[field].widget.attrs['class'] = 'border-black rounded profile-form-input'
                #self.fields[field].label = False
