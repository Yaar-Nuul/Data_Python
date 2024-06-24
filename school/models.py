from django.db import models
from django.utils import timezone

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(default=timezone.now())
    average_score = models.FloatField()
    major = models.CharField(max_length=50)
    image = models.ImageField()
    stream = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
