from django.conf import settings
from django.db import models


class Snippet(models.Model):
    class Meta:
        db_table = "snippets"

    title = models.CharField("タイトル", max_length=128)
    # フォームフィールドの空の値のエントリーを許容
    # https://docs.djangoproject.com/ja/3.2/ref/models/fields/#blank
    code = models.TextField("コード", blank=True)
    description = models.TextField("説明", blank=True)
    # ユーザが削除されたら cascade で削除される
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE
    )
    # オブジェクトが最初に作成されたときに自動で現在を設定
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    # オブジェクトが保存されるたび自動で現在を設定
    # https://docs.djangoproject.com/ja/3.2/ref/models/fields/#datefield
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self) -> str:
        return self.title
