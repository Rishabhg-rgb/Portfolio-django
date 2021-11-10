from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Phone = models.IntegerField(max_length=12)
    Project = models.CharField(max_length=100)
    Message = models.TextField()
    
    def __str__(self):
        return self.Name