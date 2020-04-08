from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=140)
    book = models.TextField()
    image = models.ImageField(upload_to='book/')

    def __str__(self):
        return self.title