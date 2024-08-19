from django.utils import timezone
from rest_framework import serializers
from .models import Task, SubTask, Category


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ('created_at',)


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, data):
        if self.instance and Category.objects.filter(name=data['name']).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        elif not self.instance and Category.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return data


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline']

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Deadline cannot be in the past.")
        return value