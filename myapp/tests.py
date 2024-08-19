from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from datetime import timedelta


class TaskTests(APITestCase):
    def test_create_task(self):
        data = {
            'title': 'Test Task',
            'description': 'Description',
            'status': 'new',
            'deadline': timezone.now() + timedelta(days=3)
        }
        response = self.client.post('/tasks/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
