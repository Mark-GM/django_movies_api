from django.db import models
from django.db.models import fields
from pinterest.models import Movie
from rest_framework import serializers

# serializers.Serializer
# serializers.ModelSerializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # acts as all fields except id field
        # exclude = ['id']