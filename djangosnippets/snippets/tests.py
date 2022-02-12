from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.urls import resolve

from snippets.models import Snippet
from snippets.views import snippet_edit, snippet_new, top

UserModel = get_user_model()


class TopPageTest(TestCase):
    def test_top_page_returns_200_and_title(self):
        res = self.client.get("/")
        self.assertContains(res, "Djangoスニペット", status_code=200)

    def test_top_page_uses_expected_template(self):
        res = self.client.get("/")
        self.assertTemplateUsed(res, "snippets/top.html")


class TopPageRenderSnippetsTest(TestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.snippet = Snippet.objects.create(
            title="title1",
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )

    def test_return_snippet_title(self):
        """作成したスニペットのタイトルが含まれること"""
        req = RequestFactory().get("/")
        req.user = self.user
        res = top(req)
        self.assertContains(res, self.snippet.title)

    def test_return_username(self):
        req = RequestFactory().get("/")
        req.user = self.user
        res = top(req)
        self.assertContains(res, self.user.username)


class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        actual = resolve("/snippets/new/")
        self.assertEqual(snippet_new, actual.func)


class SnippetDetailTest(TestCase):
    # 各テストメソッドの直前に呼び出される
    def setUp(self) -> None:
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
        )
        self.snippet = Snippet.objects.create(
            title="title1",
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )

    def test_use_expected_template(self):
        res = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(res, "snippets/snippet_detail.html")

    def test_returns_200_and_expected_heading(self):
        """スニペットのタイトルが含まれること"""
        res = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertContains(res, self.snippet.title, status_code=200)


class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        actual = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit, actual.func)
