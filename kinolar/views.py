from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import (
        CreateRatingSerializer,
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

class AddStarRatingView(APIView):
    def get_ip_client(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if  x_forwarded_for:
            ip =  x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(ip=self.get_ip_client(request))
        return Response(serializer.data, status=201)
      