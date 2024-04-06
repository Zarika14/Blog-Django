from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50, unique=True, null = False, blank=False)
    description = models.TextField(null = False, blank=False)
    image = models.ImageField(upload_to='images/',default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
