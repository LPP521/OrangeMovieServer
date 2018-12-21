from django.db import models

# Create your models here.

# class Category(models.Model):
#     name = models.CharField('category name', max_length=50, unique=True)

#     def __str__(self):
#         return self.name

class Tag(models.Model):
    name = models.CharField('tag name', max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField('actor name', max_length=100, unique=True, blank=False)
    photo = models.ImageField('photo', upload_to='images')

    def __str__(self):
        return self.name

class Membership(models.Model):
    actor = models.ForeignKey(Actor, verbose_name='actor', on_delete=models.CASCADE, related_name='memberships', related_query_name='memberships')
    role = models.CharField('role', max_length=100)

    def __str__(self):
        return str(self.actor) + ":" + self.role

class Movie(models.Model):
    name = models.CharField('name', max_length=100, blank=False)
    ename = models.CharField('english name', max_length=100)
    cover = models.ImageField('cover', upload_to='images')
    rating = models.FloatField('rating', default=0.0)
    popularity = models.IntegerField('popularity', default=0)
    info = models.CharField('info', max_length=50)
    release_date = models.DateTimeField('release date')
    plot = models.TextField('plot')
    on_sale = models.BooleanField(default=True)

    # category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='tags', related_name='movies', related_query_name='movies')
    members = models.ManyToManyField(Membership, verbose_name='members', related_name='movies', related_query_name='movies')

    class Meta:
        ordering = ('-release_date', '-rating', '-popularity', 'name')

    def __str__(self):
        return self.name

