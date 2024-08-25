from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskTests(APITestCase):

    def test_create_task(self):
        url = reverse('task-list-create')
        data = {'title': 'New Task', 'description': 'Task Description', 'status': 'Pending', 'deadline': '2024-12-31T23:59:59Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks(self):
        url = reverse('task-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
