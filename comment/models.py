from django.db import models
from user.models import WXUser
from movie.models import Movie

# Create your models here.

class Comment(models.Model):
    content = models.TextField('body')
    post_date = models.DateTimeField('post time', auto_now_add=True)
    
    post = models.ForeignKey(Movie, verbose_name='commented post', on_delete=models.CASCADE)
    author = models.ForeignKey(WXUser, verbose_name='author', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return self.content[:20]