from django import forms 
from .models import Website

class WebsiteForm(forms.ModelForm):
    longurl = forms.URLField(required=True)
    
    class Meta:
        model = Website
        fields = ('longurl',)