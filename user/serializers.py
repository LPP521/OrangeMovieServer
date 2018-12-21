from rest_framework import serializers
from .models import *

class AvatarField(serializers.ImageField):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        url = value.url
        print(url)
        if url.find('http') != -1:
            return url[7:].replace('%3A', ':/')
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url

class WXUserSerializer(serializers.ModelSerializer):
    avatar = AvatarField()
    class Meta:
        model = WXUser
        fields = ('pk', 'name', 'avatar')

    def create(self, validated_data):
        # print(validated_data)
        instance = WXUser.objects.create()
        instance.name = validated_data.get('name')
        instance.avatar = validated_data.get('avatar')
        instance.save()
        return instance

class CoverField(serializers.ImageField):
    def to_representation(self, value):
        url = value.url
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url

class TicketSerializer(serializers.ModelSerializer):
    ticket = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ('ticket',)

    def get_ticket(self, obj):
        request = self.context.get('request', None)
        data = {}
        data['movie'] = obj.scene.movie.name
        data['cover'] = request.build_absolute_uri(obj.scene.movie.cover.url)
        data['info'] = obj.scene.movie.info
        data['theater'] = obj.scene.theater.name
        data['date'] = obj.scene.start.strftime("%Y-%m-%d")
        data['start'] = obj.scene.start.strftime("%H:%M")
        data['end'] = obj.scene.end.strftime("%H:%M")
        data['info'] = obj.scene.movie.info
        data['row'] = obj.row
        data['col'] = obj.col
        data['effect'] = obj.scene.effect
        data['hall'] = obj.scene.hall
        return data

class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        instance = Ticket.objects.create()
        instance.user = WXUser.objects.get(name=validated_data.get('user'))
        instance.scene = Scene.objects.get(pk=validated_data.get('sence'))
        instance.row = validated_data.get('row')
        instance.col = validated_data.get('col')
        seats = validated_data.get('seats')
        for seat in seats:
            instance.row = seat.row
            instance.col = seat.col
            instance.save()
        return instance
