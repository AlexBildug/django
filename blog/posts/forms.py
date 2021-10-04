from django import forms

from shop.models import ORDER_BY_CHOICES


class RegistrationForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=ORDER_BY_CHOICES,
        widget=forms.Select(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    age = forms.IntegerField(min_value=18, required=False)
