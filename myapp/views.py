from django.utils import timezone
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import SubTask
from .serializers import TaskDetailSerializer, SubTaskCreateSerializer
from .pagination import CustomPagination
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Task
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = Task.objects.filter(category=category).count()
        return Response({'task_count': task_count})


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TaskStatsView(generics.GenericAPIView):
    def get(self, request):
        total_tasks = Task.objects.count()
        tasks_by_status = Task.objects.values('status').annotate(count=Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()
        data = {
            'total_tasks': total_tasks,
            'tasks_by_status': list(tasks_by_status),
            'overdue_tasks': overdue_tasks
        }
        return Response(data)


class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


class SubTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer


from django.http import HttpResponse


def hello(request):
    return HttpResponse("Ну привет а теперь поменяй на bye")


def bye(request):
    return HttpResponse("Все, Прощай (>_<) можешь еще ввести admin если ты админ конечно)")


def home(request):
    return HttpResponse("Привет! добавь hello в строку ")
