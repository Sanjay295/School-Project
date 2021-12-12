from django.db import models

# Create your models here.
class stud(models.Model):
    s_name = models.CharField(max_length=30)
    f_name = models.CharField(max_length=30)
    s_DOB = models.IntegerField()
    s_class = models.CharField(max_length=30)
    s_address = models.CharField(max_length=30)
    s_school = models.CharField(max_length=30)
    s_email = models.EmailField(max_length=30)
    s_city = models.CharField(max_length=30)
    s_state = models.CharField(max_length=30)
    s_pin = models.IntegerField()