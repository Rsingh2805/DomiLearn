from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Stories')
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
