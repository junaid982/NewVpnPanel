from django.urls import path
from . import views



urlpatterns = [
    path('get_app/' , views.getapp_api),
]