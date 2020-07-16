from django.http import HttpResponse


def index(request):
    resp = HttpResponse('<h1>Главная страница проекта Book</h1>')
    return resp
