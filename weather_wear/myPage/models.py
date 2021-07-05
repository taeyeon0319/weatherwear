from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import sys
sys.path.append("..")
from django.conf import settings

# Create your models here.


#자기 착장 기록

class MyClothes(models.Model):
    id=models.AutoField(primary_key=True)
    #제목
    title=models.CharField(max_length=300)
    #날씨 카테고리
    WEATHER_CHOICE=(
        ('sunny','맑음'),
        ('cloud','흐림'),
        ('rain','비'),
        ('snow','눈'),
    )
    weather=models.CharField(max_length=20, choices=WEATHER_CHOICE, default="")
    #기온
    temperature=models.IntegerField(default=0)
    #날짜
    post_date=models.DateField()
    #작성자
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자", default="")
    thumbnail=models.ImageField(upload_to='images', blank=True, null=True, default="{%static 'images/blank.png' %}")
    memo=models.TextField(default="")


    def __str__(self):
        return self.title
    
    class Meta:
        db_table="MyClothes"
