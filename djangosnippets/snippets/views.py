from django.shortcuts import render

from snippets.models import Snippet


def top(request):
    snippets = Snippet.objects.all()
    return render(request, "snippets/top.html", {"snippets": snippets})


def snippet_new(request):
    pass


def snippet_edit(request, snippet_id):
    pass


def snippet_detail(request, snippet_id):
    pass
