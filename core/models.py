from django.db import models

# Create your models here.
class ContactedUser(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    number=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name
    

    
