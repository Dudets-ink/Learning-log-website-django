"""Определяет схемы url для learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
        path('', views.index, name='index'), # домашняя страница
        path('topics/', views.topics, name='topics'), # просмотр списка тем 
        path('topics/<int:topic_id>/', views.topic, name='topic'), # просмотр темы
        path('new_topic/', views.new_topic, name='new_topic'), # создание новой темы пользователем
        path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'), # создание новой записи пользователем
        path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'), # редактирование записи
        ]
