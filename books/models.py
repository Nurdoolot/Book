from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=140)
    book = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    text = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.post.title}, {self.username}'