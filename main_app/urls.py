from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('adventurers/', views.adventurers_index, name='index'),
    path('adventurers/<name>/', views.adventurers_detail, name='detail'),
    path('adventurers/<int:adventurer_id>/<name>/add_journey', views.add_journey, name='add_journey'),
    path('adventurers/<int:adventurer_id>/delete', views.adventurers_delete, name='adventurers_delete'),
    path('adventurers/<int:adventurer_id>/<name>/edit', views.adventurers_edit, name="adventurers_edit"),
    path('adventurers/<int:adventurer_id>/<name>/assoc_toy/<int:enemy_id>/', views.assoc_enemy, name='assoc_enemy'),
    path('adventurers/<int:adventurer_id>/<name>/deassoc_toy/<int:enemy_id>/', views.deassoc_enemy, name='deassoc_enemy'),
]