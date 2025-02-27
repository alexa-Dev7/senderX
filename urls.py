from django.urls import path
from sender.views import index, chat

urlpatterns = [
    path('', index, name='home'),
    path('chat/<str:username>/', chat, name='chat'),
]