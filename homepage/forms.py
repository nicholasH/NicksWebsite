from django import forms

class businessCardForm(forms.Form):
    email = forms.CharField(max_length=255)
    contact_name = forms.CharField(max_length=255)
    biz_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    message = forms.CharField(max_length=255)

