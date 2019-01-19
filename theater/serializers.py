from rest_framework import serializers
from .models import *
from movie.serializers import MovieSerializer
import json

class TheaterSerializer(serializers.ModelSerializer):
    # lowest = serializers.SerializerMethodField()
    class Meta:
        model = Theater
        fields = ('pk', 'name', 'city', 'address', 'reduction', 'lowest_price')

    # def get_lowest(self, obj):
    #     scenes = obj.scene_set.all()
    #     minval = 1000.0
    #     for scene in scenes:
    #         minval = min(minval, scene.price)
    #     return minval

class DateSerializerField(serializers.RelatedField):
    def to_representation(self, value):
        return value.strftime("%Y-%m-%d %H:%M")

class SceneSerializer(serializers.ModelSerializer):
    theater = TheaterSerializer()
    movie = MovieSerializer()
    start = DateSerializerField(read_only=True)
    end = DateSerializerField(read_only=True)
    class Meta:
        model = Scene
        fields = ('pk', 'theater', 'movie', 'price', 'effect', 'start', 'end', 'hall', 'seats')

class HallSerializer(serializers.ModelSerializer):
    theater = TheaterSerializer()
    class Meta:
        model = Hall
        fields = ('name', 'theater')

        
class ShopSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()

    class Meta:
        model = Theater
        fields = ('name', 'address', 'movies')

    def get_movies(self, obj):
        request = self.context.get('request', None)
        scenes = obj.scene_set.all()
        movie_list = []
        for scene in scenes:
            scene_simp = {}
            scene_simp['pk'] = scene.pk
            scene_simp['price'] = scene.price
            scene_simp['effect'] = scene.effect
            # scene_simp['start'] = scene.start.strftime("%Y-%m-%d %H:%M")
            # scene_simp['end'] = scene.end.strftime("%Y-%m-%d %H:%M")
            scene_simp['start'] = scene.start.strftime("%H:%M")
            scene_simp['end'] = scene.end.strftime("%H:%M")
            scene_simp['hall'] = scene.hall
            l = [data for data in movie_list if data.get('name')==scene.movie.name]
            if len(l) > 0:
                movie['scenes'].append(scene_simp)
            else:
                movie = {}
                movie['name'] = scene.movie.name
                movie['cover'] = request.build_absolute_uri(scene.movie.cover.url)
                movie['rating'] = scene.movie.rating
                movie['info'] = scene.movie.info
                movie['scenes'] = [scene_simp]
                movie_list.append(movie)
        return movie_list

class TheaterSerialzeField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

class DateSerializeField(serializers.RelatedField):
    def to_representation(self, value):
        return value.strftime("%Y-%m-%d %H:%M")

class SeatsSerializer(serializers.ModelSerializer):
    theater = TheaterSerialzeField(read_only=True)
    start = DateSerializeField(read_only=True)
    class Meta:
        model = Scene
        fields = ('theater', 'seats', 'hall', 'start', 'effect', 'price')

class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ('seats',)