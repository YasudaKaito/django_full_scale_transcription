from django.shortcuts import get_object_or_404, render

from snippets.models import Snippet


def top(request):
    snippets = Snippet.objects.all()
    return render(request, "snippets/top.html", {"snippets": snippets})


def snippet_new(request):
    pass


def snippet_edit(request, snippet_id):
    pass


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, "snippets/snippet_detail.html", {"snippet": snippet})
