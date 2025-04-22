from django import forms
from passport.models import Passport_type

class PassportFilterForm(forms.Form):
    Passport_type = forms.ModelChoiceField(
        queryset = Passport_type.objects.all(),
        label="Select Passport Type",
        empty_label="Choose one...",
        widget=forms.Select(attrs={"class": "form-select"})
    )
