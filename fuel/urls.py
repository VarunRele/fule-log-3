from django.urls import path
from . import views

app_name = 'fuel'
urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('edit/<int:pk>/', views.edit_log, name='edit'),
    path('delete/<int:pk>/', views.delete_log, name='delete')
]