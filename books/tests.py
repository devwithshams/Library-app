from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'A good title',
            subtitle = 'An excellent subtitle',
            author = 'John Doe',
            isbn = '1234567890123',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'A good title')
        self.assertEqual(self.book.subtitle, 'An excellent subtitle')
        self.assertEqual(self.book.author, 'John Doe')
        self.assertEqual(self.book.isbn, '1234567890123')

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detailview(self):
        response = self.client.get(reverse('book', args=[self.book.id]))
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'An excellent subtitle')
        self.assertTemplateUsed(response, 'books/book_detail.html')

    