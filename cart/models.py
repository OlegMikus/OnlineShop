from django.db import models

from books.models import Book
from customer.models import User


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class CartBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
