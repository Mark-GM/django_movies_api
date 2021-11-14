from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from pinterest.models import Movie
from .serializers import MovieSerializer
from .permissions import UserCanDeleteMovie

@api_view(["GET"])
@permission_classes([])
def hello(request):
    data = {"message": "Hello from rest api"}

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([])
def movies_list(request):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(instance=movies, many=True)

    return Response(data=serialized_movies.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([])
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serialized_movie = MovieSerializer(instance=movie)

    return Response(data=serialized_movie.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_movie(request):
    serialized_movie = MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
    else:
        return Response(
            data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST
        )

    return Response(data=serialized_movie.data, status=status.HTTP_200_OK)


@api_view(["PATCH", "PUT"])
def edit_movie(request, pk):

    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        serialized_movie = MovieSerializer(
            instance=movie, data=request.data, partial=True
        )
    elif request.method == "PUT":
        serialized_movie = MovieSerializer(instance=movie, data=request.data)

    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response(data=serialized_movie.data, status=status.HTTP_200_OK)

    return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([UserCanDeleteMovie])
def delete_movie(request, pk):

    response = {}

    try:
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        response["data"] = {"message": f"movie {movie.title} deleted successfully"}
        response["status"] = status.HTTP_200_OK
    except Exception as e:
        response["data"] = {"message": f"error while deleting movie {e}"}
        response["status"] = status.HTTP_400_BAD_REQUEST

    print(response)
    return Response(**response)
