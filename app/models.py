from django.db import models
from django.utils.timezone import now
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.
class MyData(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default="")
    data = models.CharField(max_length=250,null=True,blank=True)
    timespan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data[:25]
    