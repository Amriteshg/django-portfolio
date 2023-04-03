from django import forms

# Contact model
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    phone = forms.CharField(max_length=30)
    options = forms.CharField(max_length=30)
    concern = forms.CharField(max_length=30)