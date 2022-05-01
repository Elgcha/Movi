from unicodedata import category
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE


class Address(models.Model):
    sido = models.CharField(max_length=20)
    sigungu = models.TextField()
    dong = models.TextField()
    doro = models.TextField()

    def __str__(self):
        return self.sido + ' ' + self.sigungu + ' ' + self.dong + ' ' + self.doro

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Alarm(models.Model):
    user = models.CharField(max_length=50)
    content = models.TextField()
    check = models.BooleanField()
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)


class Delivery(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    address = models.ForeignKey(Address, on_delete=CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    state = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    moved_at = models.DateTimeField(blank=True, null=True)
    etc = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.number)