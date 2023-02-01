from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from .filters import MovieFilter
from .forms import UserRegisterForm, MyAuthenticationForm
from .models import MovieUser
from django.contrib.auth.models import User



class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('film:movie-list')
    form_class = UserRegisterForm
    
    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
    
    def get_success_message(self, cleaned_data):
        username = cleaned_data['username'].capitalize()
        return f'Salut {username} ! Merci pour ton inscription'



class SignInView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = MyAuthenticationForm

    def get_success_message(self, cleaned_data):
        return f'Salut {self.request.user.username} ! Content de te revoir'
        
    def get_default_redirect_url(self):
        return reverse_lazy('film:movie-list', kwargs={'pk': self.request.user.id} )


class MovieListView(LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('connexion')
    model = MovieUser
    template_name = 'film-list.html'
    filterset_class = MovieFilter

    def get_queryset(self):
        qs = MovieUser.objects.filter(user=self.kwargs.get('pk'))
        return qs
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['users'] = User.objects.all()
        return data