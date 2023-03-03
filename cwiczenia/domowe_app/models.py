from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Person(models.Model):
    def __str__(self):
        return f"First_name: {self.first_name}, last_name: {self.last_name}"
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

class Genre(models.Model):
    def __str__(self):
        return f"Name: {self.name}"
    name = models.CharField(max_length=32)

class Movie(models.Model):
    def __str__(self):
        return f"title: {self.title}, director: {self.director}, screenplay: {self.screenplay}," \
               f" year: {self.year}, rating: {self.rating}"
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='+')
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='+')
    starring = models.ManyToManyField(Person)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1,
                                 validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])
    genre = models.ManyToManyField(Genre)
