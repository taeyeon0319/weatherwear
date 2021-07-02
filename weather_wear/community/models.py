from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    WEATHER = (
        ('맑음', '맑음'),
        ('비', '비'),
        ('흐림', '흐림'),
        ('우박', '우박'),
        ('눈', '눈'),
        ('안개', '안개'),
        ('소나기', '소나기')
    )

    GENDER = (
        ('남자', '남자'),
        ('여자', '여자')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="community/", blank=True, null=True)
    view_count = models.PositiveIntegerField(default = 0)
    weather = models.CharField(max_length=80, choices=WEATHER)
    gender = models.CharField(max_length=2, choices=GENDER)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
