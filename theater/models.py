from django.db import models
from movie.models import Movie
from jsonfield import JSONField
from django.db.models import Min

class Theater(models.Model):
    name = models.CharField('theater name', max_length=100, blank=False)
    city = models.CharField('city', max_length=50, blank=False)
    address = models.CharField('address', max_length=100)
    reduction = models.CharField('reduction', max_length=100)

    class Meta:
        ordering = ('city', 'name')

    def __str__(self):
        return self.name
    
    @property
    def lowest_price(self):
        return self.scene_set.aggregate(lowest=Min('price'))['lowest']

class Scene(models.Model):
    theater = models.ForeignKey(Theater, verbose_name='theater', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name='movie', on_delete=models.CASCADE)

    price = models.FloatField('price', blank=False)
    effect = models.CharField('effect', max_length=50)
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    hall = models.CharField('hall name', max_length=50)
    # rows = models.IntegerField('rows')
    # cols = models.IntegerField('columns')
    # seats = models.BinaryField('seats', max_length=500)
    seats = JSONField()

    class Meta:
        ordering = ('start',)

    def __str__(self):
        return str(self.movie) + " " + self.start.strftime("%Y-%m-%d %H:%M")


class Hall(models.Model):
    name = models.CharField('hall name', max_length=50, unique=True, blank=False)
    theater = models.ForeignKey(Theater, verbose_name='theater', on_delete=models.CASCADE)
    # rows = models.IntegerField('rows')
    # cols = models.IntegerField('columns')

    def __str__(self):
        return self.name
