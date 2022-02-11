from django.http import HttpResponse
from django.test import TestCase
from django.urls import resolve

from snippets.views import snippet_detail, snippet_edit, snippet_new


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        response: HttpResponse = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response: HttpResponse = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")


class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        actual = resolve("/snippets/new/")
        self.assertEqual(snippet_new, actual.func)


class SnippetDetailTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        actual = resolve("/snippets/1/")
        self.assertEqual(snippet_detail, actual.func)


class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        actual = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit, actual.func)
