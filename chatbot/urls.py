# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('get-next-question/', views.get_next_question, name='get_next_question'),
]