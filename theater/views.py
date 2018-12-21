from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializers import *

class TheaterList(generics.ListAPIView):
    serializer_class = TheaterSerializer

    def get_queryset(self):
        queryset = Theater.objects.all()
        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city=city)
        return queryset

class TheaterDetail(generics.RetrieveAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class ShopDetail(generics.RetrieveAPIView):
    queryset = Theater.objects.all()
    serializer_class = ShopSerializer

class HallList(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class HallDetail(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class SceneList(generics.ListAPIView):
    serializer_class = SceneSerializer

    def get_queryset(self):
        queryset = Scene.objects.all()
        theater = self.request.query_params.get('theater', None)
        if theater is not None:
            queryset = queryset.filter(theater__name=theater)
        movie = self.request.query_params.get('movie', None)
        if movie is not None:
            queryset = queryset.filter(movie__name=movie)
        return queryset

class SceneDetail(generics.RetrieveAPIView):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer

class TheaterClassByCityList(generics.ListAPIView):
    serializer_class = TheaterSerializer

    def get_queryset(self):
        queryset = Theater.objects.all()
        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city=city)
        return queryset

class SeatsDetail(generics.RetrieveAPIView):
    queryset = Scene.objects.all()
    serializer_class = SeatsSerializer

class PayDetail(generics.RetrieveUpdateAPIView):
    queryset = Scene.objects.all()
    serializer_class = PaySerializer

def get_cities(request):
    cities = [
        {'class': '热门城市', 'cities': ['上海', '北京', '广州', '深圳', '武汉', '天津', '西安', '南京', '杭州', '成都', '重庆']},
        {'class': 'A', 'cities': ['阿坝', '阿克苏', '阿拉善盟', '阿勒泰', '安吉', '安康', '安宁', '安平']},
        {'class': 'B', 'cities': ['白城', '白色', '白山', '保定', '宝鸡', '保山', '包头', '巴中', '北京', '本溪', '滨海']},
        {'class': 'D', 'cities': ['大理', '大连', '郸城', '丹东', '丹阳', '大庆']},
        {'class': 'E', 'cities': ['鄂尔多斯', '峨眉山', '恩施', '鄂州']},
        {'class': 'F', 'cities': ['丰城', '奉化', '凤凰', '凤阳']},
        {'class': 'G', 'cities': ['阿坝', '阿克苏', '阿拉善盟', '阿勒泰', '安吉', '安康', '安宁', '安平']},
        {'class': 'H', 'cities': ['白城', '白色', '白山', '保定', '宝鸡', '保山', '包头', '巴中', '北京', '本溪', '滨海']},
        {'class': 'J', 'cities': ['大理', '大连', '郸城', '丹东', '丹阳', '大庆']},
        {'class': 'K', 'cities': ['鄂尔多斯', '峨眉山', '恩施', '鄂州']},
        {'class': 'L', 'cities': ['丰城', '奉化', '凤凰', '凤阳']},
        {'class': 'M', 'cities': ['阿坝', '阿克苏', '阿拉善盟', '阿勒泰', '安吉', '安康', '安宁', '安平']},
        {'class': 'N', 'cities': ['白城', '白色', '白山', '保定', '宝鸡', '保山', '包头', '巴中', '北京', '本溪', '滨海']},
        {'class': 'P', 'cities': ['大理', '大连', '郸城', '丹东', '丹阳', '大庆']},
        {'class': 'Q', 'cities': ['鄂尔多斯', '峨眉山', '恩施', '鄂州']},
        {'class': 'L', 'cities': ['丰城', '奉化', '凤凰', '凤阳']},
        {'class': 'S', 'cities': ['阿坝', '阿克苏', '阿拉善盟', '阿勒泰', '安吉', '安康', '安宁', '安平']},
        {'class': 'T', 'cities': ['白城', '白色', '白山', '保定', '宝鸡', '保山', '包头', '巴中', '北京', '本溪', '滨海']},
        {'class': 'W', 'cities': ['大理', '大连', '郸城', '丹东', '丹阳', '大庆']},
        {'class': 'X', 'cities': ['鄂尔多斯', '峨眉山', '恩施', '鄂州']},
        {'class': 'Y', 'cities': ['丰城', '奉化', '凤凰', '凤阳']},
        {'class': 'Z', 'cities': ['阿坝', '阿克苏', '阿拉善盟', '阿勒泰', '安吉', '安康', '安宁', '安平']}
    ]
    return JsonResponse(cities, safe=False)