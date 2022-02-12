from django.test import TestCase
from django.urls import resolve

from snippets.views import snippet_detail, snippet_edit, snippet_new


class TopPageTest(TestCase):
    def test_top_page_returns_200_and_title(self):
        res = self.client.get("/")
        self.assertContains(res, "Djangoスニペット", status_code=200)

    def test_top_page_uses_expected_template(self):
        res = self.client.get("/")
        self.assertTemplateUsed(res, "snippets/top.html")


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
