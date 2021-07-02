from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="community/", blank=True, null=True)

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

