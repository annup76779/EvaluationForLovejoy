import os
from datetime import datetime

from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
import logging

logger = logging.getLogger('custom')


def upload_to(instance, filename):
    # Extract file extension
    ext = filename.split('.')[-1]

    # Create a unique filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    name = slugify(instance.user.username)  # Slugify the username for clarity
    new_filename = f"{name}_{timestamp}.{ext}"

    # Define the upload path
    return os.path.join('uploads/', new_filename)


class EvaluationRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    contact_preference = models.CharField(choices=[('phone', 'Phone'), ('email', 'Email')], max_length=10)
    photo = models.ImageField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only log for new uploads
            logger.info(f"File uploaded by user: {self.user.username}, filename: {self.photo.name}")
        super().save(*args, **kwargs)
