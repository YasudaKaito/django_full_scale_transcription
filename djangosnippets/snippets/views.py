from django.shortcuts import render


def top(request):
    return render(request, "snippets/top.html")


def snippet_new(request):
    pass


def snippet_edit(request, snippet_id):
    pass


def snippet_detail(request, snippet_id):
    pass
