from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

