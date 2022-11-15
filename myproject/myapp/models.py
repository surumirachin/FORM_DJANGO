
from django.db import models
from django import forms

# Create your models here.
standard =(
    ('1','First'),
    ('2','Second'),
    ('3','Third'),
     ('4','Fourth'),
    ('5','Fifth'),
    ('6','Sixth'),
     ('7','Seventh'),
    ('8','Eigth'),
    ('9','Ninth'),
     ('10','Tenth'),
    ('11','Eleventh'),
    ('12','Twelth'),
)

class Student(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    classes = models.CharField(max_length=50,choices=standard)
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.full_name