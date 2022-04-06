from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30, default="Username")
    email = models.EmailField(max_length=100, default="abc@abc.abc", unique=True, null=False)
    phone = models.CharField(max_length=10, default="1234567890" ,unique=True)
    text = models.TextField(max_length=1000, default="feedback hear")

    def __str__(self):
        return self.email
