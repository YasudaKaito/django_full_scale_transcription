from django.http import HttpResponse


def top(request):
    return HttpResponse(b"Hello World")


def snippet_new(request):
    pass


def snippet_edit(request, snippet_id):
    pass


def snippet_detail(request, snippet_id):
    pass
