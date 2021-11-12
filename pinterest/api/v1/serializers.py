from pinterest.models import Cast, Category, Movie
from rest_framework import serializers


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ("name",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class MovieSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    cast = CastSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
        # depth = 1
        # acts as all fields except id field
        # exclude = ['id']
