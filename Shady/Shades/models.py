from statistics import mode
from traceback import print_exc
from turtle import title
from unicodedata import category
from django.conf import settings
from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('Eyeglass1'),
    ('1300'),
    ('description'),
    ('MensEyeGlasses')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=300)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)

    def __str__(self):
        return self.title