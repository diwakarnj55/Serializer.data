from django.db import models

class Mango(models.Model):
    name=models.TextField(max_length=100)
    age=models.TextField(max_length=100)
    phone=models.TextField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    def __str__(self):
        return self.name
