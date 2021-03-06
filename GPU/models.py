from django.db import models
from specifics.models import Memory, Color, TDP
# Create your models here.

class Chipset(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CoreClock(models.Model):
    clock = models.FloatField()
    unit = models.CharField(max_length=30)

    def __str__(self):
        return str(self.clock) + ' ' + self.unit


class GPU(models.Model):
    brand = models.CharField(max_length=30, null=True)
    memory = models.ForeignKey(Memory, null=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL)
    length = models.CharField(max_length=30, null=True)
    TDP = models.ForeignKey(TDP, null=True, on_delete=models.SET_NULL)
    core_clock = models.ForeignKey(CoreClock, related_name='core_clock', null=True, on_delete=models.SET_NULL)
    boost_clock = models.ForeignKey(CoreClock, related_name='boost_clock', null=True, on_delete=models.SET_NULL)
    chipset = models.ForeignKey(Chipset, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.brand + ' ' + self.chipset.__str__()
