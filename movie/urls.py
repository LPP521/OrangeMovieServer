from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('movies/', MovieList.as_view()),
    path('movies/<int:pk>/', MovieDetail.as_view()),
    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagDetail.as_view()),
    path('actors/', ActorList.as_view()),
    path('actors/<int:pk>/', ActorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)