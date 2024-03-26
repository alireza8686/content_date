from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class DaysInformation(models.Model):
    MONTH_CHOICES = [
        ('1', 'فروردین'),
        ('2', 'اردیبهشت'),
        ('3', 'خرداد'),
        ('4', 'تیر'),
        ('5', 'مرداد'),
        ('6', 'شهریور'),
        ('7', 'مهر'),
        ('8', 'ابان'),
        ('9', 'آذر'),
        ('10', 'دی'),
        ('11', 'بهمن'),
        ('12', 'اسفند'),
    ]

    YEAR_CHOICES = [
        ('1403', '1403'),
        ('1404', '1404'),
        ('1405', '1405'),
    ]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    day_number = models.IntegerField(validators=[ MaxValueValidator(31),MinValueValidator(1)])
    month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    year = models.CharField(max_length=4,choices=YEAR_CHOICES)
    content = models.TextField(max_length=100)



    class Meta:
        unique_together = [['day_number', 'month', 'year', 'user']]

    def __str__(self):
        return self.content