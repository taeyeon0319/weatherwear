from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    GENDER_CHOICE = (
        ('남자', '남자'),
        ('여자', '여자'),
    )
    BODY_FORM = (
        ('마름','마름'),
        ('보통','보통'),
        ('과체중','과체중'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=20,default='')
    gender = models.CharField(max_length=2, choices= GENDER_CHOICE)
    age = models.IntegerField(default='')
    height = models.IntegerField(default='')
    bodyForm = models.CharField(max_length=5, choices= BODY_FORM)


    class Meta:
        ordering = ['id']
        db_table = 'user_profile'

        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return self.name