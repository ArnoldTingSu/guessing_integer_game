from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('assign_username', views.assign),
    path('game', views.game),
    path('process_game', views.process_game)
]
