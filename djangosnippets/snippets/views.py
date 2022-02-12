from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from snippets.forms import SnippetForm
from snippets.models import Snippet


def top(request):
    snippets = Snippet.objects.all()
    return render(request, "snippets/top.html", {"snippets": snippets})


@login_required
def snippet_new(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, "snippets/snippet_new.html", {"form": form})


def snippet_edit(request, snippet_id):
    pass


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, "snippets/snippet_detail.html", {"snippet": snippet})
