from django.test import TestCase, Client
from django.urls import reverse

from inventory.models import BookStore
from inventory.views import seachItem

from faker import Factory

fake = Factory.create()


class ViewTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.title = 'Book 1'
        self.category = 'Art'
        self.author = 'Spears'
        self.book = BookStore(title=self.title, author=self.author, category=self.category)
        self.book.save()

    def tearDown(self):
        del self.book

    def test_add_book(self):
        title = fake.name()
        author = fake.last_name()
        response = self.client.post(reverse('book:add'), {
            "title": title,
            "author": author,
            "category": self.category
        })
        self.assertEqual(response.status_code, 200)

    def test_search_item(self):
        self.assertEqual(len(seachItem('category', 'Music')), 0)
        self.assertEqual(len(seachItem('category', 'Art')), 1)
        self.assertEqual(len(seachItem('Music', 'Art')), 0)
        self.assertEqual(len(seachItem('Music', self.title)), 1)

    def test_book_listing(self):
        response = self.client.get(reverse('book:list'))
        self.assertEqual(response.status_code, 200)
