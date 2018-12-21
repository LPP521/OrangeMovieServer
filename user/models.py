from django.db import models
from theater.models import Scene

# Create your models here.

class WXUser(models.Model):
    name = models.CharField('name', max_length=100, blank=False, unique=True)
    avatar = models.ImageField('cover', upload_to='images')

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(WXUser, on_delete=models.CASCADE)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    row = models.IntegerField('row')
    col = models.IntegerField('column')

    class Meta:
        ordering = ('-pk',)