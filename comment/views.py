from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics

from .models import *
from .serializers import *

class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        movie = self.request.query_params.get('movie', None)
        if movie is not None:
            queryset = queryset.filter(post__name=movie)
        return queryset
        
class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentClassByMovieList(generics.ListAPIView):
    serializer_class = Comment

    def get_queryset(self):
        queryset = Comment.objects.all()
        movie = self.request.query_params.get('movie', None)
        if movie is not None:
            queryset = queryset.filter(post__name=movie)
        return queryset