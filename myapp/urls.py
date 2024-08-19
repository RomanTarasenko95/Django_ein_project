from django.urls import path
from . import views
from django.urls import path
from .views import (
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView,
    TaskCreateView,
    TaskListView,
    TaskStatsView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('bye/', views.bye, name='bey'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
]
