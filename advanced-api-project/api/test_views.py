import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        # Create an Author instance
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create sample books with proper date values
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=datetime.date(1958, 1, 1),  # ✅ valid date
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="No Longer at Ease",
            publication_year=datetime.date(1960, 1, 1),
            author=self.author
        )

    # -------------------------------
    # CRUD Tests
    # -------------------------------
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    def test_create_book(self):
        url = reverse("book-create")
        data = {
            "title": "Arrow of God",
            "publication_year": "1964-01-01",  # ✅ ISO date string
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Things Fall Apart (Updated)",
            "publication_year": "1958-01-01",  # ✅ ISO date string
            "author": self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -------------------------------
    # Filtering, Searching, Ordering
    # -------------------------------
    def test_filter_books_by_year(self):
        url = reverse("book-list") + "?publication_year=1960-01-01"  # ✅ full date
        response = self.client.get(url)
        titles = [b["title"] for b in response.data]
        self.assertIn("No Longer at Ease", titles)

    def test_search_books(self):
        url = reverse("book-list") + "?search=Fall"
        response = self.client.get(url)
        titles = [b["title"] for b in response.data]
        self.assertIn("Things Fall Apart", titles)

    def test_order_books_by_year_desc(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.data[0]["title"], "No Longer at Ease")

    # -------------------------------
    # Permissions
    # -------------------------------
    def test_unauthenticated_create_book(self):
        self.client.logout()
        url = reverse("book-create")
        data = {
            "title": "Test Book",
            "publication_year": "2025-01-01",  # ✅ ISO date string
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
