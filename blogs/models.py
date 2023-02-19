from image_uploader_widget.widgets import ImageUploaderWidget
from django import forms
from django.db import models


# Patient model
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)  # primary key
    name = models.CharField(max_length=100)
    patient_photo = models.ImageField(upload_to='profile_pics/', default='default_profile_pic.png')
    age = models.IntegerField(blank=True)
    sex = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')), default='M')
    description = models.TextField(blank=True)
    visiting_date = models.DateField(
        auto_now=True, null=True)


    # to display the name instead of patient number
    def __str__(self):
        return self.name


