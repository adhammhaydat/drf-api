from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import BlogApi

class BlogApiModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_BlBlogApi =BlogApi.objects.create(
            auther = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )
        test_BlBlogApi.save()

    def test_blog_content(self):
        blogapi =BlogApi.objects.get(id=1)

        self.assertEqual(str(blogapi.auther), 'tester')
        self.assertEqual(blogapi.title, 'Title of Blog')
        self.assertEqual(blogapi.body, 'Words about the blog')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_BlogApi =BlogApi.objects.create(
            auther = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )
        test_BlogApi.save()

        response = self.client.get(reverse('detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'id')
        self.assertAlmostEqual(response.data['id'],1)


    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        url = reverse('blog_list')
        data = {
            "title":"Testing is Fun!!!",
            "body":"when the right tools are available",
            "auther":test_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(BlogApi.objects.count(), 1)
        self.assertEqual(BlogApi.objects.get().title, data['title'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_blogapi =BlogApi.objects.create(
            auther = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )

        test_blogapi.save()

        url = reverse('detail',args=[test_blogapi.id])
        data = {
            "title":"Testing is Still Fun!!!",
            "auther":test_blogapi.auther.id,
            "body":test_blogapi.body,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(BlogApi.objects.count(), test_blogapi.id)
        self.assertEqual(BlogApi.objects.get().title, data['title'])


    def test_delete(self):
        """Test the api can delete aBlogApi."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_BlBlogApi =BlogApi.objects.create(
            auther = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )

        test_BlBlogApi.save()

        blogapi =BlogApi.objects.get()

        url = reverse('detail', kwargs={'pk':blogapi.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)