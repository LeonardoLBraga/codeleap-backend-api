from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Post

class PostAPITests(APITestCase):
    """
    Test suite for the Post API endpoints.
    Includes tests for creating, listing, updating, and deleting posts.
    """

    def setUp(self):
        """
        Set up a sample post to be used in update and delete tests.
        """
        self.base_url = reverse('post-list-create')
        self.sample_data = {
            "username": "leonardo",
            "title": "My post",
            "content": "This is the content of the post"
        }
        self.post = Post.objects.create(**self.sample_data)


    def test_create_post(self):
        """
        Test that a post can be successfully created via the API.
        """
        data = {
            "username": "john",
            "title": "Test Title",
            "content": "Test Content"
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "john")
        self.assertEqual(response.data["title"], "Test Title")
        self.assertIn("created_datetime", response.data)


    def test_list_posts(self):
        """
        Test that posts can be retrieved via the API.
        """
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)


    def test_update_post(self):
        """
        Test that a post can be updated via the API using PATCH.
        """
        url = reverse('post-update-delete', kwargs={'id': self.post.id})
        data = {
            "title": "Updated Title",
            "content": "Updated Content"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated Title")
        self.assertEqual(self.post.content, "Updated Content")


    def test_delete_post(self):
        """
        Test that a post can be deleted via the API.
        """
        url = reverse('post-update-delete', kwargs={'id': self.post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())
