from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name='todo_app'),
    path('',views.main, name='main'),
    path('tasks/',views.tasks, name='tasks'),
    path('tasks/details/<int:id>',views.details, name='details'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('testing/',views.testing, name='testing'),
]
