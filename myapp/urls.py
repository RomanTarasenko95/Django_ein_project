from django.urls import path
from .views import (
    TaskListCreateView, TaskRetrieveUpdateDestroyView,
    SubTaskListCreateView, SubTaskRetrieveUpdateDestroyView,
    TaskStatsView, hello, bye, home
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail-update-delete'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail-update-delete'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('hello/', hello),
    path('bye/', bye),
    path('', home)
]
