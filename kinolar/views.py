from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import (
        MovieListSerializer, 
        MovieDetailSerializer,
        ReviewCreateSerializer
    )


class MovieListAPIView(APIView):
    """Kinolar ro`yhati"""
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
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