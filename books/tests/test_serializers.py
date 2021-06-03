from django.test import TestCase

from books.models import Category, Author, Book
from books.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
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
        book_1 = Book.objects.create(title='Test book 1',
                                     description='Test book 1 description Author 2',
                                     pub_date='1835-02-12',
                                     category=category,
                                     author=author_1,
                                     price="600.00",
                                     available=True)
        book_2 = Book.objects.create(title='Test book Author 2',
                                     description='Test book 2 description',
                                     pub_date='1835-02-27',
                                     category=category,
                                     author=author_2,
                                     price="565.00",
                                     available=True)
        book_3 = Book.objects.create(title='Test book 3',
                                     description='Test book 3 description',
                                     pub_date='1999-02-27',
                                     category=category,
                                     author=author_2,
                                     price="565.00",
                                     available=False)
        data = BookSerializer([book_1, book_2, book_3], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'title': 'Test book 1',
                'description': 'Test book 1 description Author 2',
                'pub_date': '1835-02-12',
                'price': "600.00",
                'available': True,
                'category': 1,
                'author': author_1.id,
            },
            {
                'id': book_2.id,
                'title': 'Test book Author 2',
                'description': 'Test book 2 description',
                'pub_date': '1835-02-27',
                'price': "565.00",
                'available': True,
                'category': 1,
                'author': author_2.id
            },
            {
                'id': book_3.id,
                'title': 'Test book 3',
                'description': 'Test book 3 description',
                'pub_date': '1999-02-27',
                'price': "565.00",
                'available': False,
                'category': 1,
                'author': author_2.id,
            }
        ]
        self.assertEqual(expected_data, data)
