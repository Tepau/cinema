from django.urls import path
from .views import MovieListView


app_name = 'film'

urlpatterns = [
    path('<int:pk>', MovieListView.as_view(), name='movie-list'),
]
