from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=10, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=20)
    year = models.PositiveIntegerField()

    def clean(self):
        current_year = datetime.now().year

        if self.year > current_year + 2:
            raise ValidationError('Year of manufacture cannot be more than 2 years from the current year')
        
    def __str__(self):
        return f"{self.reg_no} {self.make} {self.model}"

