from django.db import models
from users.models import CustomUser


class EvaluationRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    contact_preference = models.CharField(choices=[('phone', 'Phone'), ('email', 'Email')], max_length=10)
    photo = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.user.username} on {self.created_at}"
