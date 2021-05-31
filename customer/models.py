from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from books.models import Book


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, default='')
    age = models.IntegerField(default=0)


class Review(models.Model):
    text = models.TextField()
    user_of_review = models.ForeignKey(User, on_delete=models.CASCADE)
    book_for_review = models.ForeignKey(Book, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('book-review', kwargs={'pk': self.pk})
