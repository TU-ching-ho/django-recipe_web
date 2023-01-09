from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.title}({self.user.username})-{self.created.strftime("%Y-%m-%d %H:%M:%S")}'
        # return顯示在admin/後台登入後畫面
