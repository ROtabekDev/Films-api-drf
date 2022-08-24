from rest_framework import serializers

from .models import Movie, Review

class MovieListSerializer(serializers.ModelSerializer):
    """Kinolar ro`yhati"""
    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'category')


class MovieDetailSerializer(serializers.ModelSerializer):
    """Bitta film uchun"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True) 
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True) 
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True) 
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True) 
    
    class Meta:
        model = Movie
        exclude = ('draft',)

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"