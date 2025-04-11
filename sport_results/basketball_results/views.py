from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import BasketballMatch
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView


def match_list(request):
    matches = BasketballMatch.objects.all().order_by('-date')

    query_team = request.GET.get('team')
    query_date = request.GET.get('date')

    if query_team:
        matches = matches.filter(
            Q(team1__icontains=query_team) | Q(team2__icontains=query_team))

    if query_date:
        matches = matches.filter(date=query_date)

    return render(request, 'match_list.html', {'matches': matches, 'query_team': query_team or '', 'query_date': query_date or ''})


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Užsiregistravote sėkmingai, galite prisijungti.')
        return response


class LoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request ,'Sėkmingai prisijungėte')
        return super().form_valid(form)

class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Sėkmingai atsijungėte')
        return super().dispatch(request, *args, **kwargs)










