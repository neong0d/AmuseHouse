from rest_framework.serializers import (
    ModelSerializer,
)

from .models import Film


class FilmSerializer(ModelSerializer):
    """serializer for films watched"""

    class Meta:
        model = Film
        fields = [
            'id', 'title', 'release_year', 'rating', 'genre'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """add a new film to library"""
        film = Film.objects.create(**validated_data)
        return film

    def update(self, instance, validated_data):
        """update film details"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance