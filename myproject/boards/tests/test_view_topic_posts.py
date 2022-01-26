from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from ..models import Board, Topic, Post
from ..views import topic_posts


class TopicPostsTest(TestCase):
    def setUp(self):
        board = Board.objects.create(name="Django", description="Django board")
        user = User.objects.create_user(username="avnguyen", email="avnguyen@testmail.com", password="123")
        topic = Topic.objects.create(subject='Hello, world!', board=board, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={"pk": board.pk, "topic_pk": topic.pk})
        self.response = self.client.get(url)

    def test_topic_posts_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_topic_posts_view_function(self):
        view = resolve('/board/1/topics/1/')
        self.assertEqual(view.func, topic_posts)