from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer

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