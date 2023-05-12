from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  related_name='author_books')
    genre = models.ForeignKey(Genre, related_name='genre_books', on_delete=models.CASCADE)
    date_published = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(datetime.now().year)])
    publisher = models.CharField(max_length=255)
    page_total = models.IntegerField(validators=[MinValueValidator(1)])
    cover = models.ImageField(upload_to='book_covers', null=True, blank=True)

    def __str__(self):
        return self.name
