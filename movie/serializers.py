from rest_framework import serializers
from .models import Tag, Actor, Movie, Membership

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'photo')

class MembershipSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()
    class Meta:
        model = Membership
        fields = ('role', 'actor')

class MovieSerializer(serializers.ModelSerializer):
    members = MembershipSerializer(many=True)
    tags = TagSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('pk', 'name', 'ename', 'cover', 'rating', 'popularity', 'info',
                  'release_date', 'plot', 'on_sale', 'tags', 'members')

    def create(self, validated_data):
        members_data = validated_data.pop('members')
        tags_data = validated_data.pop('tags')
        movie = Movie.objects.create(**validated_data)
        for member_data in members_data:
            Membership.objects.create(movie=movie, **member_data)
        for tag_data in tags_data:
            Tag.objects.create(movie=movie, **tag_data)
        return movie

class TagListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

class MemberListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.actor.name

class DateSerializerField(serializers.RelatedField):
    def to_representation(self, value):
        return value.strftime("%Y-%m-%d")

class MovieIndexSerializer(serializers.ModelSerializer):
    members = MemberListingField(many=True, read_only=True)
    tags = TagListingField(many=True, read_only=True)
    release_date = DateSerializerField(read_only=True)
    class Meta:
        model = Movie
        fields = ('pk', 'name', 'ename', 'cover', 'rating', 'popularity', 'info',
                  'release_date', 'plot', 'on_sale', 'tags', 'members')

class MovieDetailSerializer(serializers.ModelSerializer):
    members = MembershipSerializer(many=True)
    tags = TagListingField(many=True, read_only=True)
    release_date = DateSerializerField(read_only=True)
    class Meta:
        model = Movie
        fields = ('pk', 'name', 'ename', 'cover', 'rating', 'popularity', 'info',
                  'release_date', 'plot', 'on_sale', 'tags', 'members')