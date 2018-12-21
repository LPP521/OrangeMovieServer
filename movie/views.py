from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics

from .models import Tag, Actor, Movie
from .serializers import *

# Create your views here.

class ActorList(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetail(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class MovieList(generics.ListAPIView):
    serializer_class = MovieIndexSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            tag = get_object_or_404(Tag, name=tag)
            queryset = queryset.filter(tags=tag)
        return queryset

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

class MovieClassByTagList(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            tag = get_object_or_404(Tag, name=tag)
            queryset = queryset.filter(tags=tag)
        return queryset



