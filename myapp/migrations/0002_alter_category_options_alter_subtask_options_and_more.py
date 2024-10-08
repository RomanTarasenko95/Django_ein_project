# Generated by Django 5.0.7 on 2024-08-05 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subtask',
            options={'ordering': ['-created_at'], 'verbose_name': 'SubTask', 'verbose_name_plural': 'SubTasks'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterUniqueTogether(
            name='subtask',
            unique_together={('title',)},
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('title',)},
        ),
        migrations.AlterModelTable(
            name='category',
            table='task_manager_category',
        ),
        migrations.AlterModelTable(
            name='subtask',
            table='task_manager_subtask',
        ),
        migrations.AlterModelTable(
            name='task',
            table='task_manager_task',
        ),
    ]
