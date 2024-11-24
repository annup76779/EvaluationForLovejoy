from django import forms
from .models import EvaluationRequest


class EvaluationRequestForm(forms.ModelForm):
    class Meta:
        model = EvaluationRequest
        fields = ['comment', 'contact_preference', 'photo']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter details about the antique item',
                'rows': 4,
            }),
            'contact_preference': forms.Select(attrs={
                'class': 'form-select',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
