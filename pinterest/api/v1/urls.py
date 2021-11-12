from django.urls import path
from .views import hello, movies_list, movie_details, create_movie, edit_movie, delete_movie

app_name = "pinterest-v1"

urlpatterns = [
    path("hello-api", hello, name="hello"),
    path("api/v1/movies", movies_list, name="movies"),
    path("api/v1/movies/<int:pk>", movie_details, name="movie-details"),
    path("api/v1/movies/create", create_movie, name="create-movie"),
    path("api/v1/movies/<int:pk>/edit", edit_movie, name="edit-movie"),
    path("api/v1/movies/<int:pk>/delete", delete_movie, name="delete-movie"),
]
