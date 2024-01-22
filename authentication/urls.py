from django.urls import path
from .views import registeration, login

urlpatterns = [
    path('register/', registeration, name='register'),
    path('login/', login, name='login'),
]
