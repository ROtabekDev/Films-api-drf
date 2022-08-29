from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models 
from rest_framework import permissions


from .models import Movie, Actor
from .serializers import (
        CreateRatingSerializer,
        MovieListSerializer, 
        MovieDetailSerializer,
        ReviewCreateSerializer,
        ActorListSerializer,
        ActorDetailSerializer
    )
from .service import MovieFilter, get_client_ip, PaginationMovie

# class MovieListAPIView(APIView):
#     """Kinolar ro`yhati"""
#     def get(self, request):
#         movies = Movie.objects.filter(draft=False).annotate(
#             rating_user=models.Count("ratings",
#                                      filter=models.Q(ratings__ip=get_client_ip(self.request)))
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
#         )  
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(data=serializer.data)

class MovieListGAPIView(generics.ListAPIView):
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    pagination_class = PaginationMovie

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )  
        return movies


# class MovieDetailAPIView(APIView):
#     """Bitta kino uchun"""
#     def get(self, request, pk):
#         movie = Movie.objects.get(id=pk)
#         serializer = MovieDetailSerializer(movie)
#         return Response(data=serializer.data)

class MovieDetailGAPIView(generics.RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.filter(draft=False)
    permission_classes = [permissions.IsAuthenticated]

# class ReviewCreateAPIView(APIView):
#     """Filmga komment qo`shish"""
#     def post(self, request):
#         review = ReviewCreateSerializer(data=request.data)
#         review.is_valid(raise_exception=True)
#         review.save()
            
#         return Response(data=review.data)

class ReviewCreateGAPIView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

# class AddStarRatingView(APIView): 

#     def post(self, request):
#         serializer = CreateRatingSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(ip=self.get_ip_client(request))
#         return Response(serializer.data, status=201)

class AddStarRatingGView(generics.CreateAPIView):
    serializer_class = CreateRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer

class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'pk' # standart o`zi 'pk'
      