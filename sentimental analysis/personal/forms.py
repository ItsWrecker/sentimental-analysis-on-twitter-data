from django import forms


class SearchForm(forms.Form):
    tags = forms.CharField(label='tags', max_length=100)

    
