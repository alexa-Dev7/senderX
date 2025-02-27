from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register_user(username, password):
    if User.objects.filter(username=username).exists():
        return "User already exists"
    User.objects.create_user(username=username, password=password)
    return "User registered successfully"

def login_user(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return "Login successful"
    return "Invalid credentials"