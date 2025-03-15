from urllib import response
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            id = 1,
            title = 'Django for APIs',
            subtitle = 'Build web APIs with Python & Django',
            author = 'William S. Vincent',
            isbn = '1234567890',
        )


    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)

    def test_api_detailview(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.book)
