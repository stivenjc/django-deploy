from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default='hola, twitter', max_length=200)
    image = models.ImageField(default='images.png')

    # images

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content
