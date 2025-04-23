from django import forms
from passport.models import Passport_type, Country

class PassportFilterForm(forms.Form):
    Passport_type = forms.ModelChoiceField(
        queryset = Passport_type.objects.all(),
        label="Select Passport Type",
        empty_label="Choose one...",
        widget=forms.Select(attrs={"class": "form-select"})
    )


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'Continent', 'Passport_type', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Continent': forms.Select(attrs={'class': 'form-select'}),
            'Passport_types': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'image': forms.URLInput(attrs={'class': 'form-control'}),
        }

