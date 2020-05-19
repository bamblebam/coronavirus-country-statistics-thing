from django import forms


class CountryForm(forms.Form):
    name = forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={'placeholder':'Country Name'}))
    