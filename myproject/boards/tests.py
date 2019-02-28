from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve

from boards.views import home, board_topics
from boards.models import Board


class HomeTests(TestCase):

    def test_home_view_status_code(self):
        """检查请求首页URL后，返回的响应状态码是否正常"""

        url = reverse('home')
        # print(url)              # /
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """检查请求首页的URL的时候，是否返回了正确的视图函数"""

        view = resolve('/')
        self.assertEqual(view.func, home)


class BoardTopicsTests(TestCase):

    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEqual(view.func, board_topics)

