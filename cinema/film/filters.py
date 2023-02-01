from django_filters import FilterSet, ChoiceFilter
from .models import Movie, MovieUser
from django.contrib.auth.models import User

all_years = []
for movie in MovieUser.objects.all():
    if (movie.date.year, movie.date.year) not in all_years:
        all_years.append((movie.date.year, movie.date.year))

YEAR_CHOICES = tuple(all_years)


class MovieFilter(FilterSet):
    year = ChoiceFilter(label='Année', field_name='date__year', choices=YEAR_CHOICES)

    class Meta:
        model = Movie
        fields = ['year']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(MovieFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['year'].field.widget.attrs = ({'class': 'form-control'})