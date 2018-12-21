from rest_framework import serializers
from .models import *
from user.serializers import WXUserSerializer
from movie.serializers import MovieSerializer

class DateSerializerField(serializers.RelatedField):
    def to_representation(self, value):
        return value.strftime("%Y-%m-%d %H:%M:%S")

class CommentSerializer(serializers.ModelSerializer):
    author = WXUserSerializer()
    post = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    post_date = DateSerializerField(read_only=True)
    class Meta:
        model = Comment
        fields = ('content', 'post_date', 'post', 'author')