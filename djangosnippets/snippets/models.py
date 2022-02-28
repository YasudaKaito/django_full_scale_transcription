from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Snippet(models.Model):
    class Meta:
        db_table = "snippets"

    title = models.CharField("タイトル", max_length=128)
    # フォームフィールドの空の値のエントリーを許容
    # https://docs.djangoproject.com/ja/3.2/ref/models/fields/#blank
    code = models.TextField("コード", blank=True)
    description = models.TextField("説明", blank=True, default="")
    # ユーザが削除されたら cascade で削除される
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE
    )
    # オブジェクトが最初に作成されたときに自動で現在を設定
    created_at = models.DateTimeField(_("Created at"), db_index=True, auto_now_add=True)
    # オブジェクトが保存されるたび自動で現在を設定
    # https://docs.djangoproject.com/ja/3.2/ref/models/fields/#datefield
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    text = models.TextField("本文", blank=False)
    commented_to = models.ForeignKey(
        Snippet, verbose_name="スニペット", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "comments"

    def __str__(self):
        return f"{self.pk} {self.title}"


class Tag(models.Model):
    name = models.CharField("タグ名", max_length=32)
    # related_query_name は filter(tag__name="hoge") 等として使う
    # related_name は snippet_obj.tags 等として参照できる
    snippets = models.ManyToManyField(
        Snippet, related_name="tags", related_query_name="tag"
    )

    class Meta:
        db_table = "tags"

    def __str__(self):
        return f"{self.pk} {self.name}"
