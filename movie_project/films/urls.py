from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_film, name='add_film'),  # Страница добавления фильма
    path('list/', views.film_list, name='film_list'),  # Страница списка фильмов
]