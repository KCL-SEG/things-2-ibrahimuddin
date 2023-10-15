"""Forms of the project."""
from django import forms
from .models import Thing


# Create your forms here.
class ThingForm(forms.Form):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        exclude = ['created_at']
        widgets = {
            'description' : forms.Textarea(),
            'quantity' : forms.NumberInput()
        }