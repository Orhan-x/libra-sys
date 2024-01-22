from django.urls import path
from .views import registeration

urlpatterns = [
    path('register/', registeration, name='register'),
]
