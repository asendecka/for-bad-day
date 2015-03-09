from django import forms

from .models import Quote

class QuoteForm(forms.ModelForm):
 
    class Meta:
        model = Quote
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={'placeholder': 'Click to enter your quote here...',
                       'rows': 5}),
        }
