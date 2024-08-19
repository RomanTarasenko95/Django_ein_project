from time import timezone

from django.http import HttpResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q
from .models import Task
from django.utils import timezone


class TaskStatsView(APIView):
    def get(self, request):
        total_tasks = Task.objects.count()
        status_counts = Task.objects.values('status').annotate(count=Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

        stats = {
            'total_tasks': total_tasks,
            'status_counts': status_counts,
            'overdue_tasks': overdue_tasks,
        }
        return Response(stats)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    ordering_fields = ['deadline', 'status']
    pagination_class = PageNumberPagination


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def hello(request):
    return HttpResponse("Ну привет а теперь поменяй на  bye")


def bye(request):
    return HttpResponse("Все, Прощай (>_<) можешь еще ввести admin если ты админ конечно)")


def home(request):
    return HttpResponse("Привет! добавь hello в строку ")