from django.urls import path

from . import views 

urlpatterns = [
    path('movie/', views.MovieListGAPIView.as_view(), name='movie-list'), 
    path('movie/<int:pk>/', views.MovieDetailGAPIView.as_view(), name='movie-detail'), 
    path('review/', views.ReviewCreateGAPIView.as_view(), name='create-review'), 
    path('rating/', views.AddStarRatingGView.as_view(), name='create-rating'), 
    path('actors/', views.ActorListAPIView.as_view(), name='actor-list'), 
    path('actor/<int:pk>/', views.ActorDetailAPIView.as_view(), name='actor-detail'), 
]