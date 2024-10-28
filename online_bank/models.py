from django.db import models

# Create your models here.

class Contact(models.Model):
    RADIO_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    ]
    
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=120)
    gender=models.CharField(max_length=30,choices=RADIO_CHOICES)
    acc_no=models.IntegerField(default=10000000)
    amount=models.FloatField(default=0.0)

    def __str__(self):
        return self.username
    
