from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return "List of active users with 'Message' button."

@login_required
def chat(request, username):
    return f"Chat interface with {username}"