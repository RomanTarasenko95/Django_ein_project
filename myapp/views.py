from django.http import HttpResponse


def hello(request):
    return HttpResponse("Ну привет а теперь поменяй на  bye")


def bye(request):
    return HttpResponse("Все, Прощай (>_<) можешь еще ввести admin если ты админ конечно)")


def home(request):
    return HttpResponse("Привет! добавь hello в строку ")