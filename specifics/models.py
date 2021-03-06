from django.db import models

# Create your models here.
class Memory(models.Model):
    capacity = models.CharField(max_length=50)

    def __str__(self):
        return self.capacity


class Color(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color


class Socket(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class TDP(models.Model):
    number = models.IntegerField()
    unit = models.CharField(max_length=30)

    def __str__(self):
        return str(self.number) + ' ' + self.unit