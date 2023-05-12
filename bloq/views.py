from rest_framework.viewsets import ModelViewSet
from .models import Author, Genre, Book
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Author, Genre, Book
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreModelViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']  # Fields to enable searching
    ordering_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Apply additional filters based on query parameters
        category = self.request.query_params.get('name')
        if category:
            queryset = queryset.filter(category=category)

        return queryset


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'genre__name']  # Fields to enable searching
    ordering_fields = ['name', 'genre']

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     # Apply additional filters based on query parameters
    #     genre = self.request.query_params.get('genre')
    #     if genre:
    #         queryset = queryset.filter(genre=genre)
    #
    #     return queryset


from django.shortcuts import render

# Create your views here.
