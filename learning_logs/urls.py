"""Определяет схемы url для learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
        path('', views.index, name='index'), # welcome page
        path('topics/', views.topics, name='topics'), # topics page
        path('topics/<int:topic_id>/', views.topic, name='topic'), # certain topic page
        path('new_topic/', views.new_topic, name='new_topic'), # topic creation page
        path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'), # entry creation page
        path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'), # entry edit page
        ]
