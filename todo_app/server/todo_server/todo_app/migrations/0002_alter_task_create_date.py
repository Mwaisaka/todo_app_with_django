# Generated by Django 4.2.16 on 2024-10-10 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]