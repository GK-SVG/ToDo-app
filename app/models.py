from django.db import models
from django.utils.timezone import now


# Create your models here.
class MyData(models.Model):
    data = models.CharField(max_length=250,null=True,blank=True)
    timespan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data[:25]
    