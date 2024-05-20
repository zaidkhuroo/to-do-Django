from django.db import models
from django.utils import timezone
# Create your models here.
class todo(models.Model):
    title= models.CharField(max_length=255)
    # complete=models.BooleanField(default=False)
    details = models.TextField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title