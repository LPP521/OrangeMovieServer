from django.contrib import admin
from .models import Tag, Actor, Movie, Membership

# Register your models here.

admin.site.register(Tag)
admin.site.register(Actor)
admin.site.register(Movie) 
admin.site.register(Membership) 