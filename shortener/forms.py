from django import forms
from .models import RezseclyURL

from .validators import validate_url

class RezForm(forms.Form):
    url = forms.CharField(
            label='',
            validators=[validate_url],
            widget = forms.TextInput(attrs={
                "placeholder": "Long URL",
                "class": "form-control"
            })
            )
