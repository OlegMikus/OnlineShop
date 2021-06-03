from django.urls import reverse
from rest_framework.test import APITestCase
from ..models import Book, Category, Author
from ..serializers import BookSerializer
from rest_framework import status


class BooksApiTestCase(APITestCase):
    def setUp(self) -> None:
        category = Category.objects.create(id=1, name='action')
        author_1 = Author.objects.create(first_name='Author 2',
                                         last_name='Author 1',
                                         fathers_name='Name',
                                         biography='Biography description',
                                         age=33,
                                         is_alive=True)
        author_2 = Author.objects.create(first_name='Author 1',
                                         last_name='Author 1',
                                         fathers_name='Name',
                                         biography='Biography description',
                                         age=33,
                                         is_alive=True)
        self.book_1 = Book.objects.create(title='Test book 1',
                                          description='Test book 1 description Author 2',
                                          pub_date='1835-02-12',
                                          category=category,
                                          author=author_1,
                                          price="600.00",
                                          available=True)
        self.book_2 = Book.objects.create(title='Test book Author 2',
                                          description='Test book 2 description',
                                          pub_date='1835-02-27',
                                          category=category,
                                          author=author_2,
                                          price="565.00",
                                          available=True)
        self.book_3 = Book.objects.create(title='Test book 3',
                                          description='Test book 3 description',
                                          pub_date='1999-02-27',
                                          category=category,
                                          author=author_2,
                                          price="565.00",
                                          available=False)

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1,
                                          self.book_2,
                                          self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'price': 565})
        serializer_data = BookSerializer([self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 2'})
        serializer_data = BookSerializer([self.book_1,
                                          self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': 'price'})
        print(response.data)
        serializer_data = BookSerializer([self.book_2,
                                          self.book_3,
                                          self.book_1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
