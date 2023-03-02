from django.db import models



class Band(models.Model):
    def __str__(self):
        return f"Id = {self.pk}, name = {self.name}, year = {self.year}, still_active = {self.still_active}, genr = {self.genre}"
    GENRE = (
        (-1, "Not defined"),
        (0, "rock"),
        (1, "metal"),
        (2, "pop"),
        (3, "hip-hop"),
        (4, "electronic"),
        (5, "reggae"),
        (6, "other")
    )
    name = models.CharField(max_length=64, null=False)
    year = models.DateField()
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=GENRE, default=-1)

class Category(models.Model):
    def __str__(self):
        return f"Id: {self.pk}, name: {self.name}, description: {self.description}"
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)

class Article(models.Model):
    def __str__(self):
        return f"title: {self.title}, author: {self.author}, date_added: {self.date_added}, status: {self.status}, start_date: {self.start_date}, end_date: {self.end_date}"
    STATUS = (
        (1, "w trakcie pisania"),
        (2, "czeka na akceptacje"),
        (3, "opublikowany")
    )
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

class Album(models.Model):
    SCORE = (
        (0, "0"),
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "*****")
    )
    title = models.CharField(max_length=64)
    issue = models.IntegerField()
    score = models.IntegerField(choices=SCORE)
