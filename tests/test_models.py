from django.test import TestCase
from faker import Factory

from inventory.models import BookStore

fake = Factory.create()

class BookStoreTestCase(TestCase):

    def setUp(self):
        self.title = fake.last_name()
        self.author = fake.name()
        self.category = 'art'


    def test_book_creation(self):
        book = BookStore(title=self.title, author=self.author, category=self.category)
        self.assertEqual(self.title, book.title)
        self.assertEqual(self.author, book.author)
        self.assertEqual(self.category, book.category)