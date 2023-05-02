from django.urls import path

from . import views

app_name = "generators"

urlpatterns = [
    path("npc_names", views.npc_name, name="npc_name"),
    path("character_generation/get_stats", views.get_stats, name="get_stats"),
    path("character_generation/create_pc", views.create_PC, name="create_pc"),
    path("character_generation/level_up_pc", views.level_up_PC, name="level_up_pc"),
]
