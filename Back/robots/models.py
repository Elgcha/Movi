from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.
class Robot(models.Model):
    name = models.CharField(max_length=20)
    state = models.TextField(blank=True, null=True)
    battery = models.IntegerField(default=100)
    
    

    def __str__(self):
        return self.name