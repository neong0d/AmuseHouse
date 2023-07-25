from rest_framework import (
    viewsets, mixins, status
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Film
from .serializers import FilmSerializer

class FilmViewSet(viewsets.ModelViewSet):
    """View for manage film APIs."""
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """retrieve films for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)