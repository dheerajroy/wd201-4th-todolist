from django.urls import path
from .views import Views


views = Views()
urlpatterns = [
    path('', views.all_tasks),
    path('all_tasks/', views.all_tasks),
    path('tasks/', views.tasks),
    path('completed_tasks/', views.completed_tasks),
    path('add-task/', views.add_task),
    path('delete-task/<int:index>/', views.delete_task),
    path('complete_task/<int:index>/', views.complete_task),
    path('delete_completed_task/<int:index>/', views.delete_completed_task)
]