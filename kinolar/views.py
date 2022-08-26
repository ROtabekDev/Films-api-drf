from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from django.db import models 

from .models import Movie, Actor
from .serializers import (
        CreateRatingSerializer,
        MovieListSerializer, 
        MovieDetailSerializer,
        ReviewCreateSerializer,
        ActorListSerializer,
        ActorDetailSerializer
    )
from .service import get_client_ip

class MovieListAPIView(APIView):
    """Kinolar ro`yhati"""
    def get(self, request):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        ) 
        print(movies)
        serializer = MovieListSerializer(movies, many=True)
        return Response(data=serializer.data)

class MovieDetailAPIView(APIView):
    """Bitta kino uchun"""
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serializer = MovieDetailSerializer(movie)
        return Response(data=serializer.data)

class ReviewCreateAPIView(APIView):
    """Filmga komment qo`shish"""
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        review.is_valid(raise_exception=True)
        review.save()
            
        return Response(data=review.data)

class AddStarRatingView(APIView): 

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(ip=self.get_ip_client(request))
        return Response(serializer.data, status=201)

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer

class ActorListAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
    # lookup_field = 'pk' # standart o`zi 'pk'
      