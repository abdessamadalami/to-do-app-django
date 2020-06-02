from tasks.views import index
from django.urls import path
from . import views

urlpatterns = [

  path('tasks/',views.index, name='list'),
  path('',views.index, name='list'),
  path('update:/<str:pk>/',views.updateTasks,name='updateTasks'),
  path('delete:/<str:pk>/',views.deleteTasks,name='deleteTasks'),

]
