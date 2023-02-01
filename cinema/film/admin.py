from django.contrib import admin
from .models import Movie, MovieUser


admin.site.register(Movie)
admin.site.register(MovieUser)