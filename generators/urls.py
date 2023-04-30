from django.urls import path

from . import views

app_name = "generators"

urlpatterns = [
    path("npc_names", views.npc_name, name="npc_name"),
    path("character_generation/get_stats", views.get_stats, name="get_stats"),
]
