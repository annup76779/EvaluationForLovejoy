from django import forms
from django.core.exceptions import ValidationError
import magic  # To check MIME type

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

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) < 10:
            raise forms.ValidationError("The comment must be at least 10 characters long.")
        return comment

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        # Check file size (limit: 2 MB)
        if photo.size > 2 * 1024 * 1024:
            raise ValidationError("The uploaded file must be less than 2 MB.")

        # Check MIME type
        mime = magic.Magic(mime=True)
        file_mime_type = mime.from_buffer(photo.read(1024))  # Read first 1KB
        allowed_mime_types = ['image/jpeg', 'image/png', 'image/gif']
        if file_mime_type not in allowed_mime_types:
            raise ValidationError("Only JPEG, PNG, and GIF image files are allowed.")

        return photo