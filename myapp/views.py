from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, Romeo")


def hello2(request):
    return HttpResponse("Hello, Romeo2")