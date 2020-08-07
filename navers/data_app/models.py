from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(null=False, blank=False, max_length=128)
    class Meta:
        ordering = ['email']

class Naver(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=50)
    birthdate = models.DateField(null=False, blank=False)
    admission_date = models.DateField(null=False, blank=False)
    job_role = models.CharField(null=False, blank=False, max_length=20)
    class Meta:
        ordering = ['name']

class Project(models.Model):
    owner = models.ForeignKey('Naver', on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=20)