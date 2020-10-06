from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('adventurers/', views.adventurers_index, name='index'),
    path('adventurers/<name>/', views.adventurers_detail, name='detail'),
    path('adventurers/<int:adventurer_id>/<name>/add_journey', views.add_journey, name='add_journey')
]