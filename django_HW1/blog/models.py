from django.db import models


class Post(models.Model):

    subject = models.CharField(max_length=100)
    name = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    responsibility = models.TextField(max_length=20)
