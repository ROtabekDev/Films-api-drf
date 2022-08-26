from django.urls import path

from . import views 

urlpatterns = [
    path('movie/', views.MovieListAPIView.as_view(), name='movie-list'), 
    path('movie/<int:pk>/', views.MovieDetailAPIView.as_view(), name='movie-detail'), 
    path('review/', views.ReviewCreateAPIView.as_view(), name='create-review'), 
    path('rating/', views.AddStarRatingView.as_view(), name='create-rating'), 
    path('actors/', views.ActorListAPIView.as_view(), name='actor-list'), 
]